from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import check_password_hash, generate_password_hash
import database
import crypto_utils
import data_protection
import cyber_offences_data
import co5_mobile_security_data
import co6_cyber_law_data
import final_assessment_data
import os

app = Flask(__name__)
app.secret_key = 'super_secret_development_key'  # Change in production

# Initialize database
database.init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        db = database.get_db()
        user = db.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()
        
        if user and check_password_hash(user['password'], password):
            session['user_id'] = user['id']
            session['username'] = user['username']
            session['is_admin'] = user['is_admin']
            flash('Logged in successfully.', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password', 'danger')
            
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        
        if password != confirm_password:
            flash('Passwords do not match.', 'danger')
            return redirect(url_for('register'))
            
        db = database.get_db()
        existing = db.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()
        
        if existing:
            flash('Username already exists.', 'danger')
            return redirect(url_for('register'))
            
        db.execute('INSERT INTO users (username, password) VALUES (?, ?)', 
                   (username, generate_password_hash(password)))
        db.commit()
        
        flash('Registration successful. Please login.', 'success')
        return redirect(url_for('login'))
        
    return render_template('register.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('dashboard.html', username=session['username'])

# ==================================================
# CO1 - Software Threats
# ==================================================
@app.route('/co1/threats')
def co1_threats():
    if 'user_id' not in session:
        return redirect(url_for('login'))
        
    db = database.get_db()
    threats = db.execute('SELECT * FROM threats').fetchall()
    return render_template('co1_threats.html', threats=threats)

@app.route('/co1/quiz', methods=['GET', 'POST'])
def co1_quiz():
    if 'user_id' not in session:
        return redirect(url_for('login'))
        
    db = database.get_db()
    
    if request.method == 'POST':
        # Simple evaluation logic for one question for demo
        question_id = request.form.get('question_id')
        user_answer = request.form.get('answer')
        
        question = db.execute('SELECT * FROM questions WHERE id = ?', (question_id,)).fetchone()
        
        is_correct = (user_answer == question['correct_option'])
        return render_template('quiz_result.html', question=question, is_correct=is_correct, user_answer=user_answer, co="CO1", return_url=url_for('co1_threats'))
        
    # Get a random CO1 question
    question = db.execute('SELECT * FROM questions WHERE co_code = "CO1" ORDER BY RANDOM() LIMIT 1').fetchone()
    return render_template('quiz.html', question=question, co="CO1", title="Threat Identification Quiz")

# ==================================================
# CO2 - Cryptography
# ==================================================
@app.route('/co2/lab', methods=['GET', 'POST'])
def co2_lab():
    if 'user_id' not in session:
        return redirect(url_for('login'))
        
    if request.method == 'POST':
        algo = request.form.get('algorithm')
        text = request.form.get('text')
        
        if algo == 'caesar':
            shift = int(request.form.get('key', 3))
            mode = request.form.get('mode', 'encrypt')
            result = crypto_utils.caesar_cipher(text, shift, mode)
            return render_template('co2_lab.html', result=True, algorithm='caesar', 
                                   original_text=text, result_text=result, mode=mode)
                                   
        elif algo == 'vigenere':
            keyword = request.form.get('key', 'SECRET')
            mode = request.form.get('mode', 'encrypt')
            result = crypto_utils.vigenere_cipher(text, keyword, mode)
            return render_template('co2_lab.html', result=True, algorithm='vigenere', 
                                   original_text=text, result_text=result, mode=mode)
                                   
        elif algo == 'hash':
            hash_algo = request.form.get('hash_algo', 'sha256')
            result = crypto_utils.generate_hash(text, hash_algo)
            return render_template('co2_lab.html', result=True, algorithm='hash', 
                                   original_text=text, result_hash=result, hash_algo=hash_algo)
                                   
        elif algo == 'rsa':
            result_data = crypto_utils.rsa_demo(text)
            return render_template('co2_lab.html', result=True, algorithm='rsa',
                                   original_text=text, rsa_data=result_data)
                                   
    return render_template('co2_lab.html', result=False)

# ==================================================
# CO3 - Data Protection
# ==================================================
@app.route('/co3/protection', methods=['GET', 'POST'])
def co3_protection():
    if 'user_id' not in session:
        return redirect(url_for('login'))
        
    result_password = None
    result_masking = None
    original_text = ""
    masked_text = ""
    
    if request.method == 'POST':
        action = request.form.get('action')
        
        if action == 'password':
            pwd = request.form.get('password')
            result_password = data_protection.check_password_strength(pwd)
            # IMPORTANT: Do not store or reflect the plaintext password back to the user
            
        elif action == 'masking':
            original_text = request.form.get('sensitive_text')
            masked_text = data_protection.mask_sensitive_data(original_text)
            result_masking = True
            
    return render_template('co3_protection.html', 
                           result_password=result_password, 
                           result_masking=result_masking,
                           original_text=original_text,
                           masked_text=masked_text)

# ==================================================
# CO4 - Cyber Offences
# ==================================================
@app.route('/co4/offences')
def co4_offences():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('co4_offences.html', offences=cyber_offences_data.offences)

@app.route('/co4/assessment', methods=['GET', 'POST'])
def co4_assessment():
    if 'user_id' not in session:
        return redirect(url_for('login'))
        
    scenario = cyber_offences_data.scenarios[0]
    
    if request.method == 'POST':
        score = 0
        total = len(scenario['questions'])
        results = []
        
        for i, q in enumerate(scenario['questions']):
            user_ans = request.form.get(f'q_{i}')
            is_correct = (user_ans == q['answer'])
            if is_correct:
                score += 1
            results.append({
                'question': q['q'],
                'user_ans': user_ans,
                'correct_ans': q['answer'],
                'is_correct': is_correct,
                'explanation': q['explanation']
            })
            
        return render_template('co4_assessment_result.html', scenario=scenario, results=results, score=score, total=total)
        
    return render_template('co4_assessment.html', scenario=scenario)

# ==================================================
# CO5 - Mobile & Wireless Security
# ==================================================
@app.route('/co5/mobile')
def co5_mobile():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('co5_mobile.html', topics=co5_mobile_security_data.topics)

@app.route('/co5/quiz', methods=['GET', 'POST'])
def co5_quiz():
    if 'user_id' not in session:
        return redirect(url_for('login'))
        
    quiz_data = co5_mobile_security_data.quiz
    
    if request.method == 'POST':
        score = 0
        total = len(quiz_data['questions'])
        results = []
        
        for i, q in enumerate(quiz_data['questions']):
            user_ans = request.form.get(f'q_{i}')
            is_correct = (user_ans == q['answer'])
            if is_correct:
                score += 1
            results.append({
                'question': q['q'],
                'user_ans': user_ans,
                'correct_ans': q['answer'],
                'is_correct': is_correct,
                'explanation': q['explanation']
            })
            
        return render_template('co5_quiz_result.html', quiz_title=quiz_data['title'], results=results, score=score, total=total)
        
    return render_template('co5_quiz.html', quiz=quiz_data)

# ==================================================
# CO6 - Cyber Law
# ==================================================
@app.route('/co6/law')
def co6_law():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('co6_law.html', laws=co6_cyber_law_data.laws)

@app.route('/co6/assessment', methods=['GET', 'POST'])
def co6_assessment():
    if 'user_id' not in session:
        return redirect(url_for('login'))
        
    scenarios = co6_cyber_law_data.scenarios
    
    if request.method == 'POST':
        score = 0
        total = sum(len(s['questions']) for s in scenarios)
        results = []
        
        for s_idx, s in enumerate(scenarios):
            for q_idx, q in enumerate(s['questions']):
                user_ans = request.form.get(f's{s_idx}_q{q_idx}')
                is_correct = (user_ans == q['answer'])
                if is_correct:
                    score += 1
                results.append({
                    'scenario': s['scenario_text'],
                    'question': q['q'],
                    'user_ans': user_ans,
                    'correct_ans': q['answer'],
                    'is_correct': is_correct,
                    'explanation': q['explanation']
                })
            
        return render_template('co6_assessment_result.html', results=results, score=score, total=total)
        
    return render_template('co6_assessment.html', scenarios=scenarios)

# ==================================================
# FINAL ASSESSMENT & CO COVERAGE
# ==================================================
@app.route('/assessment', methods=['GET', 'POST'])
def final_assessment():
    if 'user_id' not in session:
        return redirect(url_for('login'))
        
    questions = final_assessment_data.questions
    
    if request.method == 'POST':
        co_scores = {'CO1': 0, 'CO2': 0, 'CO3': 0, 'CO4': 0, 'CO5': 0, 'CO6': 0}
        total_score = 0
        results = []
        
        for i, q in enumerate(questions):
            user_ans = request.form.get(f'q_{i}')
            is_correct = (user_ans == q['answer'])
            if is_correct:
                co_scores[q['co']] += 1
                total_score += 1
                
            results.append({
                'co': q['co'],
                'question': q['q'],
                'user_ans': user_ans,
                'correct_ans': q['answer'],
                'is_correct': is_correct,
                'explanation': q['explanation']
            })
            
        # Save to database
        db = database.get_db()
        db.execute('''
            INSERT INTO scores (user_id, co1_score, co2_score, co3_score, co4_score, co5_score, co6_score, total_score)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (session['user_id'], co_scores['CO1'], co_scores['CO2'], co_scores['CO3'], 
              co_scores['CO4'], co_scores['CO5'], co_scores['CO6'], total_score))
        db.commit()
            
        return render_template('final_assessment_result.html', results=results, score=total_score, total=len(questions), co_scores=co_scores)
        
    return render_template('final_assessment.html', questions=questions)

@app.route('/co_coverage')
def co_coverage():
    if 'user_id' not in session:
        return redirect(url_for('login'))
        
    db = database.get_db()
    
    # Fetch the latest score for this user
    latest_score = db.execute('SELECT * FROM scores WHERE user_id = ? ORDER BY id DESC LIMIT 1', (session['user_id'],)).fetchone()
    
    co_data = [
        {"id": "CO1", "title": "Identify various software threats and attacks", "module": "Threat Identification", "route": "co1_threats"},
        {"id": "CO2", "title": "Apply cryptographic algorithms", "module": "Cryptography Lab", "route": "co2_lab"},
        {"id": "CO3", "title": "Apply data protection techniques", "module": "Data Protection", "route": "co3_protection"},
        {"id": "CO4", "title": "Analyze different types of cyber offences", "module": "Cyber Offence Analysis", "route": "co4_offences"},
        {"id": "CO5", "title": "Describe cybercrime issues on mobile", "module": "Mobile & Wireless Security", "route": "co5_mobile"},
        {"id": "CO6", "title": "Apply cyber law", "module": "Cyber Law & IT Act", "route": "co6_law"}
    ]
    
    return render_template('co_coverage.html', co_data=co_data, scores=latest_score)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
