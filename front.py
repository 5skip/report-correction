import streamlit as st
from selectpeople import people_select_box
test_lists = [
    'よって、以下のような結論が導ける',
    'あいうえお'
]

def show_should_correct_parts(file) -> list[str]:
    # 添削すべき箇所を示す   
    pass
    
def feedback_correct_part(input_text: str) -> str:
    # なぜいけないのかのフィードバック
    return "<h2>そうですね！</h2>"

def show_toggle_contents(target_part: str, key: int):
    st.write('以下の箇所がよくありません。なぜいけないのか考えてみましょう！')
    
    st.write(f'"{target_part}"')
    
    user_input_text = st.text_area('あなたの考えを入力してください', key=f'{i}-text-area')
    
    if st.button('送信する', key=f'{i}-button'):
        st.write(feedback_correct_part(user_input_text))
        
    
    
if __name__ == '__main__':
        
    st.title('レポート添削します')
    
    uploaded_file = st.file_uploader('PDFファイルをアップロードしてください', type='pdf')
    
    if uploaded_file is None:
        st.warning('PDFファイルをアップロードしてください')
        
    #should_correct_parts = show_should_correct_parts(uploaded_file)
    should_correct_parts = test_lists
        
    st.header('添削結果')
    st.warning(f'良くないところが{len(should_correct_parts)}箇所あります')
    
    for i, target_part in enumerate(should_correct_parts):
        with st.expander(f'{i+1}箇所目'):
            show_toggle_contents(target_part=target_part ,key=i)

    people_select_box()