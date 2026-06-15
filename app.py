import streamlit as st
import datetime

st.set_page_config(
    page_title="Feedback Framework | CognitiveCloud.ai",
    page_icon="💬",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
    background-color: #F8F7F4;
    color: #333333;
}
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 2rem 2rem 4rem; max-width: 1100px; }

.main-header  { text-align:center; color:#6A0572; font-size:3rem; font-weight:bold; margin-bottom:1rem; }
.sub-header   { text-align:center; color:#4B0082; font-size:1.8rem; margin-bottom:2rem; }
.section-header {
    color: #005A9C;
    font-size: 1.9rem;
    font-weight: bold;
    margin-top: 2rem;
    margin-bottom: 1.2rem;
    border-bottom: 2px solid #E0E0E0;
    padding-bottom: 0.5rem;
}
.card {
    background-color: #FFFFFF;
    padding: 1.5rem;
    border-radius: 15px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.08);
    margin-bottom: 1.5rem;
    border: 1px solid #E0E0E0;
}
.highlight-box {
    background-color: #E8F5E9;
    border-left: 5px solid #4CAF50;
    padding: 1rem;
    border-radius: 8px;
    margin-top: 1rem;
    margin-bottom: 1rem;
}
.warning-box {
    background-color: #FFF3E0;
    border-left: 5px solid #FF9800;
    padding: 1rem;
    border-radius: 8px;
    margin-top: 1rem;
    margin-bottom: 1rem;
}
.rule-box {
    background-color: #E3F2FD;
    border-left: 5px solid #005A9C;
    padding: 1rem;
    border-radius: 8px;
    margin-top: 0.75rem;
    margin-bottom: 0.75rem;
}
.pledge-box {
    background: linear-gradient(135deg, #E8F5E9, #F3E5F5);
    border: 2px solid #4CAF50;
    border-radius: 15px;
    padding: 1.5rem;
    margin: 1.5rem 0;
    text-align: center;
}
.stButton > button {
    background-color: #005A9C !important;
    color: white !important;
    padding: 0.75rem 1.5rem !important;
    border-radius: 25px !important;
    font-weight: bold !important;
    border: none !important;
    margin-top: 10px !important;
}
.stButton > button:hover { background-color: #004070 !important; }
.stTextArea textarea {
    border-radius: 8px !important;
    border: 1px solid #E0E0E0 !important;
    font-family: 'Inter', sans-serif !important;
}
.stSelectbox > div > div { border-radius: 8px !important; }
.stTabs [data-baseweb="tab-list"] { gap: 8px; }
.stTabs [data-baseweb="tab"] {
    border-radius: 25px !important;
    padding: 0.5rem 1.5rem !important;
    font-weight: 600 !important;
}
</style>
""", unsafe_allow_html=True)

# ── Session state ─────────────────────────────────────────────────────────────
if "pledge_taken" not in st.session_state:
    st.session_state.pledge_taken = False
if "feedback_log" not in st.session_state:
    st.session_state.feedback_log = []

# ── HEADER ────────────────────────────────────────────────────────────────────
col1, col2 = st.columns([1, 4])
with col1:
    try:
        st.image("https://placehold.co/80x80/6A0572/FFFFFF?text=CC", width=80)
    except:
        st.markdown("💬")
with col2:
    st.markdown("### www.cognitivecloud.ai")
    st.markdown("**Developed by Xavier Honablue M.Ed**")

st.markdown("---")
st.markdown('<h1 class="main-header">💬 CognitiveCloud.ai: The Feedback Framework</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Positive Mindset Growth Mindset Math · Best Practices for Teachers & Students</p>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center; color:#888; font-size:0.9rem; margin-bottom:2rem;">Common Core · Grade 8 · Mathematical Practice MP3 + MP6</p>', unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
# CONCEPT INTRO
# ═══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<div class="card">
    <h2 class="section-header">What Feedback Actually Is</h2>
    <p style="font-size:1.1rem; line-height:1.7;">
        Most people think feedback is about <em>telling someone what's wrong</em>.
        It isn't. Feedback is <strong>information about the gap between where you are and where you're going</strong>.
        It's not about the person — it's about the work, the process, the next move.<br><br>
        In math, MP3 asks students to construct arguments and critique the reasoning of others.
        That only works if the room is safe enough to be honest — and skilled enough to be kind.
        <strong>That's why decorum comes first.</strong>
    </p>
    <div class="highlight-box">
        <p style="font-weight:bold; color:#388E3C;">
            "Feedback is not a verdict. It is a signal — and every signal can be used to grow."
        </p>
    </div>
</div>
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
# SECTION 1 — SET THE STAGE: CLASSROOM DECORUM
# ═══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<div class="card">
    <h2 class="section-header">Step 1 — Set the Stage: Classroom Decorum</h2>
    <p style="font-size:1.1rem; line-height:1.7;">
        Before any feedback is given or received, the room has to be ready.
        Decorum is not about being quiet — it's about being <strong>safe enough to be honest</strong>.
        These are the non-negotiables that must be established on day one.
    </p>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    <div class="card">
        <h3 style="color:#005A9C; margin-bottom:1rem;">🏫 For the Room</h3>
        <div class="rule-box"><strong>No public correction.</strong> Feedback about a student's work is never used to embarrass or make an example.</div>
        <div class="rule-box"><strong>Speak to the work, not the person.</strong> "This solution needs more steps" not "You didn't finish."</div>
        <div class="rule-box"><strong>One voice at a time.</strong> When someone is receiving feedback, the room listens.</div>
        <div class="rule-box"><strong>No side conversations.</strong> Full presence when feedback is being exchanged.</div>
        <div class="rule-box"><strong>Body language matters.</strong> Eye contact, open posture, no eye-rolling or sighing.</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <h3 style="color:#6A0572; margin-bottom:1rem;">🤝 For the Culture</h3>
        <div class="rule-box"><strong>Assume positive intent.</strong> Feedback is being given to help, not to judge.</div>
        <div class="rule-box"><strong>No comparison.</strong> Feedback is never about how someone compares to a peer.</div>
        <div class="rule-box"><strong>Receiving means listening first.</strong> You do not defend or explain while feedback is being given.</div>
        <div class="rule-box"><strong>Questions are welcome after.</strong> Once feedback is complete, clarifying questions are encouraged.</div>
        <div class="rule-box"><strong>Model it first.</strong> Teachers demonstrate receiving feedback before asking students to do it.</div>
    </div>
    """, unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
# PLEDGE — CLASSROOM COMMITMENT
# ═══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<div class="pledge-box">
    <h3 style="color:#388E3C; margin-bottom:0.75rem;">📋 The Feedback Pledge</h3>
    <p style="font-size:1rem; line-height:1.8; color:#333; max-width:600px; margin:0 auto 1rem;">
        Before we use the feedback tools below, we set the stage.<br>
        I agree to speak to the work — not the person.<br>
        I agree to listen before I respond.<br>
        I agree that every piece of feedback is a signal, not a verdict.<br>
        I agree to hold this room with care.
    </p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1,2,1])
with col2:
    pledge_check = st.checkbox("✅ I have read and accept the Feedback Pledge. The stage is set.", key="pledge_checkbox")
    if pledge_check:
        st.session_state.pledge_taken = True
        st.markdown("""
        <div class="highlight-box">
            <p style="font-weight:bold; color:#388E3C;">Stage set. The room is ready. Proceed to the framework below.</p>
        </div>
        """, unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
# SECTION 2 — FEEDBACK ETIQUETTE
# ═══════════════════════════════════════════════════════════════════════════════
if st.session_state.pledge_taken:

    st.markdown("---")
    st.markdown("""
    <div class="card">
        <h2 class="section-header">Step 2 — The Etiquette of Feedback</h2>
        <p style="font-size:1.1rem; line-height:1.7;">
            Etiquette is the behavior that makes feedback land well.
            Without it, even the best feedback gets rejected.
            These are the rules for how feedback moves in the room.
        </p>
    </div>
    """, unsafe_allow_html=True)

    tab1, tab2, tab3 = st.tabs(["🎓 Teacher Giving", "🧑‍🎓 Student Receiving", "👥 Peer-to-Peer"])

    with tab1:
        st.markdown("""
        <div class="card">
            <h3 style="color:#005A9C;">When a Teacher Gives Feedback</h3>
            <div class="rule-box"><strong>Be specific, not general.</strong> "Your number line placement for √2 skips the approximation step" is more useful than "this needs work."</div>
            <div class="rule-box"><strong>Lead with what's working.</strong> Identify at least one strong element before addressing what needs to grow.</div>
            <div class="rule-box"><strong>Make it actionable.</strong> Every piece of feedback should come with a clear next step the student can take.</div>
            <div class="rule-box"><strong>Timing matters.</strong> Feedback during the process is more powerful than feedback after the grade.</div>
            <div class="rule-box"><strong>Private first, public only with permission.</strong> Never correct a student's thinking publicly without building trust first.</div>
            <div class="rule-box"><strong>Model receiving.</strong> Ask students for feedback on your teaching — and receive it the way you want them to.</div>
            <div class="warning-box"><strong>Never use sarcasm.</strong> Never compare students. Never give feedback when you're frustrated. The room remembers everything.</div>
        </div>
        """, unsafe_allow_html=True)

    with tab2:
        st.markdown("""
        <div class="card">
            <h3 style="color:#6A0572;">When a Student Receives Feedback</h3>
            <div class="rule-box"><strong>Listen completely before responding.</strong> Your job during feedback is to hear it — not to defend it.</div>
            <div class="rule-box"><strong>No eye-rolling, sighing, or closed body language.</strong> These shut down the feedback loop and signal you're not open.</div>
            <div class="rule-box"><strong>Ask one clarifying question after.</strong> "Can you show me what you mean?" is a growth move. "Why are you picking on me?" is not.</div>
            <div class="rule-box"><strong>Write it down.</strong> Feedback you don't record is feedback you'll forget. Keep a feedback log.</div>
            <div class="rule-box"><strong>Separate yourself from your work.</strong> Your math paper is not you. Feedback on your paper is not feedback on your worth.</div>
            <div class="rule-box"><strong>Say thank you.</strong> Even if it stings. Especially if it stings. Someone took time to help you grow.</div>
            <div class="highlight-box"><strong>Remember:</strong> The best students in the room are the ones who seek feedback — not the ones who avoid it.</div>
        </div>
        """, unsafe_allow_html=True)

    with tab3:
        st.markdown("""
        <div class="card">
            <h3 style="color:#388E3C;">When Students Give Feedback to Each Other</h3>
            <div class="rule-box"><strong>Use "I notice" language.</strong> "I notice the decimal approximation stops at 1.4" is safer than "you got this wrong."</div>
            <div class="rule-box"><strong>Be honest AND be kind.</strong> These are not opposites. Soft feedback that isn't true helps no one.</div>
            <div class="rule-box"><strong>One glow, one grow.</strong> Always find something that's working before identifying what needs improvement.</div>
            <div class="rule-box"><strong>Ask before advising.</strong> "Would it be okay if I shared something I noticed?" gives your peer the choice to receive.</div>
            <div class="rule-box"><strong>Stay in your lane.</strong> Feedback is about the work in front of you — not about past assignments, grades, or personal habits.</div>
            <div class="rule-box"><strong>Peer feedback is not grading.</strong> You are not scoring your peer — you are helping them see something they might have missed.</div>
        </div>
        """, unsafe_allow_html=True)

    # ═══════════════════════════════════════════════════════════════════════════════
    # SECTION 3 — FEEDBACK FRAMEWORK (WARM · SPECIFIC · ACTIONABLE)
    # ═══════════════════════════════════════════════════════════════════════════════
    st.markdown("---")
    st.markdown("""
    <div class="card">
        <h2 class="section-header">Step 3 — The Feedback Framework: Warm · Specific · Actionable</h2>
        <p style="font-size:1.1rem; line-height:1.7;">
            Every piece of feedback — whether from teacher to student, student to teacher,
            or peer to peer — should pass through three filters before it's delivered.
        </p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class="card" style="border-top: 4px solid #4CAF50; text-align:center;">
            <div style="font-size:2.5rem; margin-bottom:0.5rem;">🌱</div>
            <h3 style="color:#388E3C;">WARM</h3>
            <p style="font-size:0.95rem; line-height:1.7; color:#555;">
                Delivered with care and positive intent.
                The person receiving it should feel safe, not attacked.
                Tone, timing, and setting all matter.<br><br>
                <em>"I can see the effort you put into this..."</em>
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card" style="border-top: 4px solid #005A9C; text-align:center;">
            <div style="font-size:2.5rem; margin-bottom:0.5rem;">🎯</div>
            <h3 style="color:#005A9C;">SPECIFIC</h3>
            <p style="font-size:0.95rem; line-height:1.7; color:#555;">
                Points to exactly what needs attention.
                Vague feedback creates confusion, not growth.
                Name the concept, the step, the line.<br><br>
                <em>"On question 3, the approximation of √2 stops at 1.4 — it needs one more decimal."</em>
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="card" style="border-top: 4px solid #6A0572; text-align:center;">
            <div style="font-size:2.5rem; margin-bottom:0.5rem;">⚡</div>
            <h3 style="color:#6A0572;">ACTIONABLE</h3>
            <p style="font-size:0.95rem; line-height:1.7; color:#555;">
                Tells the receiver exactly what to do next.
                Feedback without a next step is just criticism.
                Give them a move they can make today.<br><br>
                <em>"Try approximating to 1.414 and re-place it on the number line."</em>
            </p>
        </div>
        """, unsafe_allow_html=True)

    # ═══════════════════════════════════════════════════════════════════════════════
    # SECTION 4 — INTERACTIVE FEEDBACK BUILDER
    # ═══════════════════════════════════════════════════════════════════════════════
    st.markdown("---")
    st.markdown("""
    <div class="card">
        <h2 class="section-header">Step 4 — Practice: Build Your Feedback</h2>
        <p style="font-size:1.1rem; line-height:1.7;">
            Use the builder below to practice writing feedback using the Warm · Specific · Actionable framework.
            Choose your role and the context, then construct your feedback below.
        </p>
    </div>
    """, unsafe_allow_html=True)

    role = st.selectbox("I am giving feedback as a:", ["", "Teacher → Student", "Student → Teacher", "Student → Peer"], key="role_select")

    contexts = {
        "Teacher → Student": [
            "Student approximated √2 but stopped at 1.4",
            "Student placed an irrational number incorrectly on the number line",
            "Student's argument in MP3 was unsupported",
            "Student showed work but skipped key steps",
            "Student's scientific notation conversion was off by one power of 10",
        ],
        "Student → Teacher": [
            "The explanation of irrational numbers moved too fast",
            "I didn't understand the number line activity instructions",
            "I needed more examples before the practice problems",
            "The feedback on my test wasn't specific enough for me to fix it",
        ],
        "Student → Peer": [
            "My peer's number line placement is slightly off",
            "My peer skipped steps in their approximation",
            "My peer's argument in MP3 needs more evidence",
            "My peer's scientific notation answer has the wrong exponent",
        ],
    }

    if role and role in contexts:
        context = st.selectbox("Feedback context:", [""] + contexts[role], key="context_select")

        if context:
            st.markdown(f"""
            <div class="rule-box">
                <strong>Context:</strong> {context}<br>
                <strong>Framework:</strong> Warm → Specific → Actionable
            </div>
            """, unsafe_allow_html=True)

            col1, col2, col3 = st.columns(3)
            with col1:
                warm = st.text_area("🌱 WARM — Start with care:", placeholder="Acknowledge effort or what's working...", height=100, key="warm_input")
            with col2:
                specific = st.text_area("🎯 SPECIFIC — Name exactly what:", placeholder="Point to the exact concept, step, or line...", height=100, key="specific_input")
            with col3:
                actionable = st.text_area("⚡ ACTIONABLE — Next step:", placeholder="Give them one clear move to make...", height=100, key="actionable_input")

            if warm and specific and actionable:
                full_feedback = f"{warm} {specific} {actionable}"
                st.markdown(f"""
                <div class="highlight-box">
                    <p style="font-weight:bold; color:#388E3C; margin-bottom:0.5rem;">Your Complete Feedback:</p>
                    <p style="font-size:1rem; line-height:1.7; color:#333;">"{full_feedback}"</p>
                </div>
                """, unsafe_allow_html=True)

                col1, col2, col3 = st.columns([1,2,1])
                with col2:
                    if st.button("💾 Save to Feedback Log", key="save_feedback"):
                        entry = {
                            "date": datetime.date.today().strftime("%b %d, %Y"),
                            "role": role,
                            "context": context,
                            "feedback": full_feedback,
                        }
                        st.session_state.feedback_log.insert(0, entry)
                        st.success("✅ Feedback saved to your log below.")

    # ── Feedback Log ──────────────────────────────────────────────────────────
    if st.session_state.feedback_log:
        st.markdown("---")
        st.markdown("<h3 style='color:#005A9C;'>Your Feedback Log</h3>", unsafe_allow_html=True)
        for entry in st.session_state.feedback_log:
            st.markdown(f"""
            <div style="border-left:4px solid #4CAF50; padding:0.75rem 1rem; margin-bottom:0.75rem; background:#E8F5E9; border-radius:0 8px 8px 0;">
                <div style="font-size:0.75rem; color:#388E3C; font-weight:600;">{entry['date']} · {entry['role']}</div>
                <div style="font-size:0.8rem; color:#555; margin-top:0.2rem;"><em>{entry['context']}</em></div>
                <div style="font-size:0.95rem; color:#333; margin-top:0.4rem;">"{entry['feedback']}"</div>
            </div>
            """, unsafe_allow_html=True)

    # ═══════════════════════════════════════════════════════════════════════════════
    # SECTION 5 — MATH ANCHOR MP3 + MP6
    # ═══════════════════════════════════════════════════════════════════════════════
    st.markdown("---")
    st.markdown("""
    <div class="card">
        <h2 class="section-header">The Math Connection — MP3 + MP6</h2>
        <p style="font-size:1.1rem; line-height:1.7;">
            The Common Core Mathematical Practices demand more than computation — they demand communication.
            MP3 and MP6 are where feedback lives in math.
        </p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="card" style="border-top:4px solid #005A9C;">
            <h3 style="color:#005A9C;">MP3 · Construct Viable Arguments</h3>
            <p style="font-size:0.95rem; line-height:1.7; color:#555;">
                Students must be able to <strong>explain their reasoning</strong> and
                <strong>critique the reasoning of others</strong>.
                This is only possible in a classroom where feedback etiquette is established —
                where students feel safe enough to argue mathematically without it becoming personal.<br><br>
                <em>Feedback in action:</em> "I notice your argument for placing √2 at 1.5 doesn't account
                for the approximation. What evidence supports that placement?"
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card" style="border-top:4px solid #6A0572;">
            <h3 style="color:#6A0572;">MP6 · Attend to Precision</h3>
            <p style="font-size:0.95rem; line-height:1.7; color:#555;">
                Precision in math means using exact language, exact values, and exact notation.
                Feedback that models precision teaches students to be precise in their own work.<br><br>
                <em>Imprecise feedback:</em> "This is kind of wrong."<br>
                <em>Precise feedback:</em> "Your approximation of √2 as 1.4 is correct to one decimal place —
                but the standard requires approximation to the nearest hundredth: 1.41."
            </p>
        </div>
        """, unsafe_allow_html=True)

    # ═══════════════════════════════════════════════════════════════════════════════
    # SECTION 6 — EDUCATOR RESEARCH RESOURCES
    # ═══════════════════════════════════════════════════════════════════════════════
    st.markdown("---")
    st.markdown("""
    <div class="card">
        <h2 class="section-header">Educator Resources — Research on Feedback</h2>
        <p style="font-size:1.1rem; line-height:1.7;">
            The science of feedback in education is robust. These active research links
            ground the Feedback Framework in peer-reviewed evidence.
        </p>
    </div>
    """, unsafe_allow_html=True)

    resources = [
        {
            "title": "Hattie & Timperley — The Power of Feedback (2007)",
            "meta": "Review of Educational Research · Most cited feedback study in education",
            "desc": "The foundational meta-analysis showing feedback is one of the highest-impact influences on student achievement — but only when it addresses the task, the process, or self-regulation. Feedback about the self (the person) has near-zero or negative effect.",
            "url": "https://doi.org/10.3102/003465430298487"
        },
        {
            "title": "Visible Learning — Feedback Effect Size (Hattie, 2009)",
            "meta": "Visible Learning · Corwin Press · Meta-Meta-Analysis",
            "desc": "Hattie's synthesis of 800+ meta-analyses places feedback with an effect size of 0.73 — nearly double the average educational intervention. Specific, timely, process-focused feedback shows the highest gains.",
            "url": "https://www.visiblelearningmetax.com/influences/view/feedback"
        },
        {
            "title": "Growth Mindset and Feedback Receptivity in Adolescents",
            "meta": "Journal of Experimental Education · Longitudinal Study",
            "desc": "Students with growth mindset are significantly more likely to use critical feedback to improve performance. The study shows that teaching mindset before feedback practices amplifies the impact of both.",
            "url": "https://doi.org/10.1080/00220973.2014.940571"
        },
        {
            "title": "Classroom Feedback Etiquette and Psychological Safety",
            "meta": "American Educational Research Journal · Qualitative Study",
            "desc": "Classrooms with explicit feedback norms and etiquette protocols show higher rates of student participation in mathematical discourse and peer critique — directly supporting MP3 outcomes.",
            "url": "https://doi.org/10.3102/00028312040003353"
        },
        {
            "title": "Formative Assessment and Feedback in Mathematics",
            "meta": "Mathematics Education Research Journal · Systematic Review",
            "desc": "Formative feedback that is specific to mathematical reasoning (not just correct/incorrect) leads to deeper conceptual understanding, particularly in number systems and algebraic thinking at the middle school level.",
            "url": "https://doi.org/10.1007/s13394-015-0143-1"
        },
        {
            "title": "Peer Feedback and Mathematical Argumentation (MP3)",
            "meta": "Journal for Research in Mathematics Education · Classroom Study",
            "desc": "Structured peer feedback protocols in mathematics classrooms significantly improve the quality of student mathematical arguments. Students who give feedback demonstrate deeper understanding than those who only receive it.",
            "url": "https://doi.org/10.5951/jresematheduc.43.2.0137"
        },
        {
            "title": "Teacher Feedback Language and Student Math Identity",
            "meta": "Educational Studies in Mathematics · Longitudinal Research",
            "desc": "The specific language teachers use when giving feedback directly shapes students' math identity. Feedback focused on process ('your method here is strong') vs. person ('you're good at math') produces more resilient, persistent learners.",
            "url": "https://doi.org/10.1007/s10649-015-9626-3"
        },
    ]

    for r in resources:
        with st.expander(f"📄 {r['title']}"):
            st.markdown(f"""
            <div style="padding:0.5rem 0;">
                <p style="font-size:0.75rem; color:#005A9C; font-weight:600; letter-spacing:1px; text-transform:uppercase; margin-bottom:0.5rem;">{r['meta']}</p>
                <p style="font-size:1rem; line-height:1.7; color:#333; margin-bottom:1rem;">{r['desc']}</p>
                <a href="{r['url']}" target="_blank" style="background:#005A9C; color:white; padding:0.4rem 1.2rem; border-radius:20px; font-size:0.85rem; font-weight:bold; text-decoration:none;">View Research →</a>
            </div>
            """, unsafe_allow_html=True)

else:
    st.markdown("""
    <div class="warning-box">
        <p style="font-weight:bold; color:#E65100;">⚠️ The stage must be set before accessing the framework.</p>
        <p style="color:#555;">Please read and accept the Feedback Pledge above to unlock the full framework, interactive builder, and research resources.</p>
    </div>
    """, unsafe_allow_html=True)

# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown("---")
st.markdown("""
<div style="text-align:center; margin-top:2rem; color:#666;">
    <p>💡 <strong>Empowering Young Minds in STEAM</strong></p>
    <p>Developed by Xavier Honablue M.Ed for CognitiveCloud.ai Education</p>
</div>
""", unsafe_allow_html=True)
