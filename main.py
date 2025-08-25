import pyautogui
import time


def find_and_click(image_path, confidence=0.8, duration=0.2):
    """
    화면에서 주어진 이미지를 찾아 중앙을 클릭하는 함수
    """
    try:
        # 화면 전체에서 이미지 검색
        location = pyautogui.locateCenterOnScreen(image_path, confidence=confidence)
        if location:
            pyautogui.click(location, duration=duration)
            print(f"'{image_path}' 이미지를 클릭했습니다.")
            return True
        else:
            # 이미지를 찾지 못한 경우 메시지를 출력하지 않음 (주기적인 확인을 위해)
            return False
    except Exception as e:
        print(f"이미지 인식 중 오류 발생: {e}")
        return False


def start_new_game():
    """
    새로운 10분 래피드 게임을 시작하는 함수
    """
    print("새로운 10분 게임을 시작합니다...")
    # 1. '10분 플레이' 버튼을 찾아서 클릭
    if find_and_click('start_button.png'):
        print("게임을 시작했습니다. 게임이 끝날 때까지 대기합니다.")
        return True

    print("'start_button.png'를 찾을 수 없습니다. 5초 후 다시 시도합니다.")
    return False


def main():
    """
    메인 실행 함수
    """
    print("Chess.com 자동 게임 시작 매크로를 시작합니다.")
    print("프로그램을 종료하려면 터미널(콘솔)에서 Ctrl+C를 누르세요.")

    
    while not start_new_game():
        time.sleep(5)

   
    while True:
        try:
            # 게임이 끝났는지 주기적으로 확인 ('새 게임' 버튼이 보이면 게임 종료로 간주)
            if find_and_click('new_game_button.png', confidence=0.9):
                print("게임 종료를 감지했습니다.")
                time.sleep(3)  # 잠시 대기 후 새 게임 시작

                # 새 게임이 시작될 때까지 반복 시도
                while not start_new_game():
                    time.sleep(5)

            # 10초마다 화면을 체크
            time.sleep(10)

        except KeyboardInterrupt:
            print("프로그램을 종료합니다.")
            break
        except Exception as e:
            print(f"예상치 못한 오류가 발생했습니다: {e}")
            time.sleep(10)


if __name__ == "__main__":
    main()
