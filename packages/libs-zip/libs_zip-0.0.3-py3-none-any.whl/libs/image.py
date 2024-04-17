import pyautogui
import glob
import os
from PIL import Image

# 스크린 캡처
def capture_screen(save_path=None):

    screenshot = pyautogui.screenshot()

    # 파일 이름 생성
    file_name = input("파일 이름 입력: ")

    # 저장 경로 설정
    if save_path:
        save_path = os.path.join(save_path, file_name)
    else:
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
        save_path = os.path.join(desktop_path, file_name)

    # 이미지 파일 저장
    screenshot.save(save_path)

    return save_path

# 이미지 크기 조정
def resize_image(file_path):
    # 파일이 지정된 이미지 확장자인지 확인
    if file_path.endswith(('JPG', 'JPEG', '.jpg', '.jpeg', '.png', '.bmp')):
        # 파일 이름에서 확장자 제거
        name = file_path.split(".")[0]
   
        # 이미지 열기
        image = Image.open(file_path)
        
        # 이미지 크기 조정
        width = int(input("width: "))
        height = int(input("height: "))
        resized_img = image.resize((width, height))
        
        # 조정된 이미지를 지정한 폴더에 저장
        resized_img.save(os.path.join(file_path, str(name) + f'{width}x{height}.png'))
        
        # 작업 완료 메시지 출력
        print(name + ' 이미지 크기 조정 완료')


# 폴더의 png파일들을 pdf파일로 변환
def png_to_pdf(folder_path):
    image_files = glob.glob(folder_path)

    images = []
    for img_path in image_files:
        img = Image.open(img_path)
        images.append(img)

    save_path  = input("저장 경로 입력: ")
    images[0].save(save_path, save_all = True, append_images = images[1:])



