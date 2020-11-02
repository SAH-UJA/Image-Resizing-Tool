import streamlit
import base64
import cv2
from PIL import Image

def main():
	streamlit.markdown("""# Welcome to Image Resizing Tool""")
	banner = cv2.imread('newplot.png')
        streamlit.image(banner)
	img = streamlit.file_uploader("Upload your image", type=['jpg'])
	if img:
		im = Image.open(img)
		im.save('buff.jpg')
		width = streamlit.slider("width", min_value=100, max_value=1000, step=10)
		height = streamlit.slider("height", min_value=100, max_value=1000, step=10)
		im = cv2.resize(cv2.imread('buff.jpg'), (width,height))
		streamlit.image(im)
		cv2.imwrite('graph.jpg', im)
		with open('graph.jpg','rb') as f:
			enc = base64.b64encode(f.read()).decode()
			html = f'<a href="data:image/jpg;base64,{enc}" download="img.jpg">Download</a>'
			streamlit.markdown(html, unsafe_allow_html=True)
if __name__=='__main__':
    main()
