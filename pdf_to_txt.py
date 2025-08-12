import fitz  # PyMuPDF
import os

def convert_pdf_to_txt(pdf_path, txt_path):
    """
    将PDF文件转换为TXT文本文件。
    """
    try:
        # 确保输出目录存在
        output_dir = os.path.dirname(txt_path)
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        doc = fitz.open(pdf_path)
        text = ""
        for page in doc:
            text += page.get_text()
        
        with open(txt_path, "w", encoding="utf-8") as text_file:
            text_file.write(text)
            
        print(f"成功将 '{pdf_path}' 转换为 '{txt_path}'")
        return True
    except Exception as e:
        print(f"转换PDF时发生错误: {e}")
        return False

if __name__ == "__main__":
    pdf_file = "论文/16774_SynCSE_Enhanced_Contrast.pdf"
    txt_file = "论文/16774_SynCSE_Enhanced_Contrast.txt"
    convert_pdf_to_txt(pdf_file, txt_file)
