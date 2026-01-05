"""
S.A.F.E. WebGuard - 金融欺诈防御系统
商赛演示应用 - Streamlit Cloud 版本
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import random
import time

# 设置页面
st.set_page_config(
    page_title="S.A.F.E. WebGuard",
    page_icon="🛡️",
    layout="wide"
)

# 初始化状态
if 'page' not in st.session_state:
    st.session_state.page = 'home'
if 'risk_score' not in st.session_state:
    st.session_state.risk_score = 25

# 侧边栏
with st.sidebar:
    st.title("🛡️ S.A.F.E. WebGuard")
    st.caption("金融欺诈防御系统")
    
    st.markdown("---")
    
    # 导航按钮
    if st.button("🏠 首页", use_container_width=True):
        st.session_state.page = 'home'
    if st.button("💸 交易护航", use_container_width=True):
        st.session_state.page = 'transaction'
    if st.button("🧠 AI智能", use_container_width=True):
        st.session_state.page = 'ai'
    if st.button("🏢 机构面板", use_container_width=True):
        st.session_state.page = 'dashboard'
    
    st.markdown("---")
    st.metric("活跃银行", "8家", "+2")
    st.metric("今日防护", "1,428笔", "3.2%")

# 首页
if st.session_state.page == 'home':
    st.markdown("# 🛡️ S.A.F.E. WebGuard")
    st.markdown("#### 金融欺诈防御系统 - 商赛演示版")
    
    # 创新亮点
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.info("### 🔐 零知识证明\n银行间无需共享数据即可协同风控")
    
    with col2:
        st.info("### 🤖 联邦学习\n去中心化AI训练保护隐私")
    
    with col3:
        st.info("### ⛓️ 区块链\n不可篡改审计追踪")
    
    # 快速演示
    st.markdown("## 🎯 快速演示")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 💰 风险检测")
        scenario = st.selectbox("选择场景", ["正常转账", "投资存款", "加密货币"])
        amount = st.slider("金额(HKD)", 1000, 1000000, 50000)
        
        if st.button("🔍 开始检测", type="primary"):
            with st.spinner("分析中..."):
                time.sleep(1)
                
                if "投资" in scenario or "加密" in scenario:
                    score = random.randint(70, 95)
                    color = "red"
                    message = "🚨 高风险警报"
                else:
                    score = random.randint(10, 40)
                    color = "green"
                    message = "✅ 低风险"
                
                st.session_state.risk_score = score
                st.success(f"{message} - 风险评分: {score}/100")
    
    with col2:
        st.markdown("### 📊 风险仪表盘")
        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=st.session_state.risk_score,
            title={'text': "风险评分"},
            gauge={'axis': {'range': [0, 100]}}
        ))
        st.plotly_chart(fig, use_container_width=True)

# 交易护航页面
elif st.session_state.page == 'transaction':
    st.title("💸 实时交易护航")
    
    col1, col2 = st.columns(2)
    
    with col1:
        trans_type = st.selectbox(
            "交易类型",
            ["转账给朋友", "支付供应商", "投资理财", "加密货币"]
        )
        amount = st.number_input("金额(HKD)", 1000, 1000000, 50000)
    
    with col2:
        bank = st.selectbox("收款银行", ["汇丰", "中银", "恒生", "渣打"])
        user_type = st.selectbox("用户类型", ["普通", "企业", "老年", "新居民"])
    
    if st.button("🚀 开始扫描", type="primary"):
        progress_bar = st.progress(0)
        for i in range(100):
            progress_bar.progress(i + 1)
            time.sleep(0.01)
        
        if "加密" in trans_type or amount > 100000:
            score = random.randint(75, 95)
            st.error(f"🚨 高风险: {score}/100 - 建议暂停交易")
        elif "投资" in trans_type:
            score = random.randint(40, 75)
            st.warning(f"⚠️ 中等风险: {score}/100 - 请确认信息")
        else:
            score = random.randint(10, 40)
            st.success(f"✅ 低风险: {score}/100 - 可以继续")

# AI智能页面
elif st.session_state.page == 'ai':
    st.title("🧠 AI欺诈智能")
    
    st.markdown("### 🔮 欺诈预测")
    
    data = pd.DataFrame({
        "欺诈类型": ["AI语音诈骗", "虚拟资产诈骗", "冒充诈骗", "发票欺诈"],
        "概率": ["87%", "74%", "69%", "63%"],
        "目标群体": ["中年投资者", "年轻用户", "新移民", "企业"],
        "防御策略": ["声纹验证", "平台白名单", "官方验证", "区块链验证"]
    })
    
    st.dataframe(data, use_container_width=True)
    
    st.markdown("### 📈 趋势分析")
    
    months = ['1月', '2月', '3月', '4月', '5月', '6月']
    df = pd.DataFrame({
        '月份': months,
        '投资诈骗': [45, 48, 52, 55, 58, 62],
        '冒充诈骗': [32, 35, 38, 40, 42, 45]
    })
    
    st.line_chart(df.set_index('月份'))

# 机构面板页面
elif st.session_state.page == 'dashboard':
    st.title("🏢 机构协作面板")
    
    # 指标
    col1, col2, col3, col4 = st.columns(4)
    with col1: st.metric("今日查询", "1,428", "+3.2%")
    with col2: st.metric("响应时间", "0.8秒", "-12%")
    with col3: st.metric("准确率", "96.2%", "+1.8%")
    with col4: st.metric("预防案件", "84起", "+18%")
    
    # 银行排名
    st.markdown("### 🏆 银行排名")
    
    bank_data = pd.DataFrame({
        "银行": ["汇丰银行", "中银香港", "恒生银行", "渣打银行"],
        "安全评分": [925, 872, 821, 785],
        "警报数": [142, 128, 98, 87],
        "等级": ["金牌", "金牌", "银牌", "银牌"]
    })
    
    st.dataframe(bank_data, use_container_width=True)
    
    # 案例
    st.markdown("### 🔍 案件洞察")
    
    case_data = pd.DataFrame({
        "案件类型": ["AI语音诈骗", "虚拟资产诈骗", "跨境洗钱"],
        "严重程度": ["高", "高", "中"],
        "状态": ["处理中", "已解决", "调查中"]
    })
    
    st.dataframe(case_data, use_container_width=True)

# 页脚
st.markdown("---")
st.caption("🛡️ S.A.F.E. WebGuard | 金融欺诈防御系统 | © 2024")