import streamlit as st
from datetime import datetime

# 1. CẤU HÌNH HỆ THỐNG
st.set_page_config(page_title="Thư Viện Số Thầy Hậu", layout="wide")

st.markdown("""
    <style>
    /* ÉP NỀN TRẮNG */
    .stApp { background-color: #FFFFFF !important; }
    
    /* ÉP CHỮ ĐEN CHO TOÀN BỘ CỘT PHẢI */
    h1, h2, h3, h4, p, span, div, label, .stMarkdown {
        color: #000000 !important;
        -webkit-text-fill-color: #000000 !important;
    }

    /* KHUNG NỘI DUNG SÁCH */
    .noidung-sach {
        background-color: #F8F9FA !important;
        padding: 30px !important;
        border-radius: 12px !important;
        border: 1px solid #D1D5DB !important;
        color: #000000 !important;
        font-size: 20px !important;
        line-height: 1.8 !important;
    }

    /* SIDEBAR (CỘT TRÁI) */
    section[data-testid="stSidebar"] { background-color: #F1F5F9 !important; }
    section[data-testid="stSidebar"] * { color: #000000 !important; }

    /* NÚT BẤM */
    .stButton>button {
        background-color: #1E40AF !important;
        color: #FFFFFF !important;
        font-weight: bold !important;
        border-radius: 8px;
    }
    .stButton>button p { color: #FFFFFF !important; }
    </style>
    """, unsafe_allow_html=True)

# 2. DỮ LIỆU SÁCH
DATA_BOOK = {
    "Lời nói đầu": """Có những con người không cần bước lên sân khấu lớn vẫn khiến người khác kính trọng. Có những cuộc đời không ồn ào nhưng để lại dấu ấn sâu sắc trong lòng bao thế hệ...""",
    "Chương 1: Tuổi thơ": """Ngày 7 tháng 9 năm 1978, tại phường Tân Lộc – vùng đất hiền hòa của Thành phố Cần Thơ – cậu bé Trần Trung Hậu chào đời...""",
    "Chương 2: Bước chân vào nghề": "Năm 2000, thầy Trần Trung Hậu chính thức bước vào nghề giáo...",
    "Chương 5: Câu chuyện": "Trong hành trình dạy học, có những niềm vui lớn...",
    "Kết luận": "Giữa đời thường, có những con người sống lặng lẽ mà lớn lao."
}

if 'comments' not in st.session_state:
    st.session_state.comments = []

# 3. GIAO DIỆN CHÍNH (CỘT PHẢI)
st.markdown("<h1 style='text-align: center;'>📚 THƯ VIỆN SỐ THẦY HẬU</h1>", unsafe_allow_html=True)

# Sidebar
st.sidebar.markdown("## 📖 MỤC LỤC")
selected = st.sidebar.radio("Chọn chương:", list(DATA_BOOK.keys()))

# Nội dung
st.markdown(f"<h2 style='color: #1E40AF !important;'>📌 {selected}</h2>", unsafe_allow_html=True)
content = DATA_BOOK[selected]
st.markdown(f"<div class='noidung-sach'>{content}</div>", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# 4. PHẦN BÌNH LUẬN (FIX LỖI KEYERROR)
st.markdown("### 💬 Bạn đọc nhận xét")

with st.form("form_comment", clear_on_submit=True):
    name_user = st.text_input("Tên của anh/chị:")
    comment_user = st.text_area("Cảm nhận:")
    btn = st.form_submit_button("GỬI BÌNH LUẬN")
    
    if btn and name_user and comment_user:
        # Lưu vào session với key 'text' để đồng bộ
        st.session_state.comments.insert(0, {
            "name": name_user,
            "text": comment_user,
            "time": datetime.now().strftime("%d/%m/%Y %H:%M")
        })
        st.rerun()

# Hiển thị danh sách bình luận
for c in st.session_state.comments:
    st.markdown(f"""
        <div style='background-color: #F3F4F6; padding: 15px; border-radius: 10px; margin-bottom: 10px; border-left: 5px solid #1E40AF;'>
            <strong style='color: #1E40AF !important;'>👤 {c['name']}</strong> <small>({c['time']})</small><br>
            <p style='color: #000000 !important; margin-top: 5px;'>{c['text']}</p>
        </div>
    """, unsafe_allow_html=True)
