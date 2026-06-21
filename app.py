import streamlit as st
import plotly.graph_objects as go

st.set_page_config(page_title="The Dhoni Myth", layout="wide")

st.title("🏏 The Dhoni Myth")
st.subheader("Did MS Dhoni win because of his teammates, or despite them?")

st.markdown("""
MS Dhoni is one of cricket's most debated captains. I analyzed ball-by-ball data 
from **188 ODI matches** during his captaincy era (2007–2014) to test four 
specific claims about his leadership.
""")

# Executive Summary
st.markdown("---")
st.subheader("Executive Summary")
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Overall Win Rate", "60.7%", "105 Wins")
with col2:
    st.metric("Matches Analyzed", "188", "2007–2014")
with col3:
    st.metric("Biggest Dependency", "Gambhir", "-15.6%")
with col4:
    st.metric("Batting Position Gap", "27%", "Early vs Late")

st.markdown("---")

# ---- Finding 1: Overall win rate (TEXT LEFT, CHART RIGHT) ----
st.header("📊 Finding 1 — Overall Win Rate as Captain")

col1, col2 = st.columns([1, 1.4])
with col1:
    st.markdown("""
    ### What This Means
    
    A win rate above 55% is considered excellent for an ODI captain.
    
    **60.7% puts Dhoni in the elite tier.** It's a statistically strong record that suggests genuine captaincy ability.
    
    The question isn't whether he was successful—he clearly was. The question is *why*.
    
    The next three findings dig deeper into the mechanisms of his success.
    """)
    
with col2:
    fig1 = go.Figure(data=[go.Pie(
        labels=['Wins', 'Losses', 'No Result/Tie'],
        values=[105, 68, 15],
        hole=0.6,
        marker=dict(colors=['#5DCAA5', '#F0997B', '#888780']),
        textinfo='label+percent',
        textfont=dict(size=14, color='#e8e6e0')
    )])
    fig1.add_annotation(text="60.7%", x=0.5, y=0.5,
                        font=dict(size=28, color='#5DCAA5', family='Arial Black'), showarrow=False)
    fig1.update_layout(plot_bgcolor='#252523', paper_bgcolor='#252523',
                        font=dict(color='#e8e6e0', size=12),
                        height=420, margin=dict(l=30, r=30, t=50, b=50))
    st.plotly_chart(fig1, use_container_width=True)

st.markdown("---")

# ---- Finding 2: Teammate impact (CHART LEFT, TEXT RIGHT) ----
st.header("👥 Finding 2 — The Gambhir Dependency")

col1, col2 = st.columns([1.4, 1])
with col1:
    players = ['Tendulkar', 'Kohli', 'Yuvraj', 'Sehwag', 'Gambhir']
    with_rates = [61.1, 60.6, 62.3, 63.4, 67.0]
    without_rates = [60.4, 60.8, 57.6, 58.8, 51.4]

    fig2 = go.Figure()
    fig2.add_trace(go.Bar(x=players, y=with_rates, name='With Player', 
                          marker_color='#5DCAA5', text=[f'{v}%' for v in with_rates],
                          textposition='outside', textfont=dict(size=11)))
    fig2.add_trace(go.Bar(x=players, y=without_rates, name='Without Player',
                          marker_color='#F0997B', text=[f'{v}%' for v in without_rates],
                          textposition='outside', textfont=dict(size=11)))
    fig2.update_layout(yaxis_title="Win Rate (%)", barmode='group',
                        bargap=0.3, bargroupgap=0.15,
                        yaxis=dict(gridcolor='rgba(150,150,150,0.1)'),
                        plot_bgcolor='#252523', paper_bgcolor='#252523',
                        font=dict(color='#e8e6e0', size=11),
                        height=400, legend=dict(orientation='h', y=1.05, font=dict(size=9)),
                        margin=dict(l=0, r=0, t=20, b=60))
    st.plotly_chart(fig2, use_container_width=True)

with col2:
    st.markdown("""
    ### Key Finding
    
    Most teammates had **minimal impact**. Win rates barely differed with or without them.
    
    #### Gambhir is Different
    - **With him:** 67.0%
    - **Without him:** 51.4%
    - **Impact:** -15.6% ⚠️
    
    This is the only player whose absence significantly hurt India's record. It suggests Dhoni's success wasn't evenly distributed across his squad.
    
    **Interpretation:** Dhoni's captaincy was less about having a superstar-studded team and more about maximizing specific key players.
    """)

st.markdown("---")

# ---- Finding 3: Chasing vs Defending (TEXT LEFT, CHART RIGHT) ----
st.header("⚔️ Finding 3 — The Chase Master Myth")

col1, col2 = st.columns([1, 1.4])
with col1:
    st.markdown("""
    ### The Narrative vs Reality
    
    Everyone talks about Dhoni's "chase mastery"—his legendary ability to finish games under pressure.
    
    **The data tells a different story.**
    
    #### The Numbers
    - **Defending:** 62.5% win rate
    - **Chasing:** 59.4% win rate
    - **Gap:** +3.1% in favor of defending
    
    This doesn't mean he was bad at chasing. 59.4% is still solid. It just means the myth was overblown.
    
    **Takeaway:** Dhoni was excellent in both scenarios, but marginally better when setting the tone early.
    """)

with col2:
    fig3 = go.Figure(data=[go.Bar(
        x=['Defending', 'Chasing'], y=[62.5, 59.4],
        marker_color=['#5DCAA5', '#F0997B'],
        text=['62.5%', '59.4%'], textposition='outside',
        textfont=dict(size=16, color='white'), width=0.5
    )])
    fig3.update_layout(yaxis_title="Win Rate (%)",
                        yaxis=dict(gridcolor='rgba(150,150,150,0.1)', range=[0, 75]),
                        plot_bgcolor='#252523', paper_bgcolor='#252523',
                        font=dict(color='#e8e6e0', size=12),
                        height=400, showlegend=False,
                        margin=dict(l=0, r=0, t=0, b=0))
    st.plotly_chart(fig3, use_container_width=True)

st.markdown("---")

# ---- Finding 4: Batting position (CHART LEFT, TEXT RIGHT) ----
st.header("🏏 Finding 4 — Batting Position & Win Rate")

col1, col2 = st.columns([1.4, 1])
with col1:
    fig4 = go.Figure(data=[go.Bar(
        x=['Early<br>(Pos 1–5)', 'Late<br>(Pos 6+)'], y=[73.0, 46.1],
        marker_color=['#5DCAA5', '#F0997B'],
        text=['73.0%', '46.1%'], textposition='outside',
        textfont=dict(size=16, color='white'), width=0.4
    )])
    fig4.update_layout(yaxis_title="Win Rate (%)",
                        yaxis=dict(gridcolor='rgba(150,150,150,0.1)', range=[0, 85]),
                        plot_bgcolor='#252523', paper_bgcolor='#252523',
                        font=dict(color='#e8e6e0', size=12),
                        height=400, showlegend=False,
                        margin=dict(l=0, r=0, t=0, b=0))
    st.plotly_chart(fig4, use_container_width=True)

with col2:
    st.markdown("""
    ### The Most Surprising Finding
    
    **27 percentage point difference.**
    
    This is massive.
    
    - **Early (top 5):** 73.0% win rate
    - **Late (6+):** 46.1% win rate
    
    India won nearly 3 in 4 games when Dhoni came in early, but **less than half when he batted late.**
    
    This challenges the popular strategy narrative: maybe coming in late as a finisher wasn't actually the optimal approach.
    """)

st.markdown("---")

# Conclusion
st.subheader("Conclusion")
st.markdown("""
The data reveals a nuanced picture:

1. **Dhoni was genuinely excellent** — 60.7% is elite-tier captaincy.
2. **His success wasn't evenly distributed** — it heavily depended on one key player (Gambhir).
3. **The "chase master" myth is overstated** — he was slightly better at defending.
4. **Batting position mattered significantly** — early entry correlated with much higher win rates.

The myth isn't that Dhoni was overrated. It's that **the reasons for his success are more specific than commonly believed.**
""")

st.markdown("---")
st.caption("Data source: [Cricsheet.org](https://cricsheet.org) | Analysis of 188 ODI matches (2007–2014)")