import streamlit
import base64
import cv2
from PIL import Image

def main():
	streamlit.markdown("""# Welcome to Image Resizing Tool""")
	enc_str = ""
	with open('newplot.png','rb') as f:
		enc_str = base64.b64encode(f.read()).decode()
	html = f'<img src="data:image/png;base64,{enc_str}">'
	streamlit.markdown(html, unsafe_allow_html=True)
	img = streamlit.file_uploader("Upload your image", type=['png'])
	if img:
		im = Image.open(img)
		im.save('buff.png')
		width = streamlit.slider("width", min_value=100, max_value=1000, step=10)
		height = streamlit.slider("height", min_value=100, max_value=1000, step=10)
		im = cv2.resize(cv2.imread('buff.png'), (width,height))
		streamlit.image(im)
		cv2.imwrite('graph.jpeg', im)
		with open('graph.jpeg','rb') as f:
			enc = base64.b64encode(f.read()).decode()
			html = f'<a href="data:file/jpeg;base64,{enc}" download="img.jpeg">Download</a>'
			streamlit.markdown(html, unsafe_allow_html=True)
if __name__=='__main__':
    main()
