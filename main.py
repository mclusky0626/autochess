import pyautogui
import time

def find_and_click(image_path, confidence=0.8, duration=0.2):
    """
    화면에서 주어진 이미지를 찾아 중앙을 클릭하는 함수
    """
    try:
        location = pyautogui.locateCenterOnScreen(image_path, confidence=confidence)
        if location:
            pyautogui.click(location, duration=duration)
            print(f"'{image_path}' 이미지를 클릭했습니다.")
            return True
        return False
    except Exception as e:
        print(f"이미지 인식 중 오류 발생: {e}")
        return False

def main():
    """
    메인 실행 함수
    """
    print("Chess.com 자동 게임 시작 매크로를 시작합니다.")
    print("프로그램을 종료하려면 터미널(콘솔)에서 Ctrl+C를 누르세요.")

    # --- 1단계: 첫 게임 시작 ---
    print("\n첫 게임 시작을 시도합니다...")
    # 'start_button.png' (10분 플레이 버튼)를 찾을 때까지 5초 간격으로 계속 시도
    while not find_and_click('start_button.png'):
        print("'start_button.png'를 찾을 수 없습니다. 5초 후 다시 시도합니다.")
        time.sleep(5)
    
    print("\n첫 게임을 시작했습니다. 이제부터 게임 종료를 감지합니다.")
    time.sleep(10) # 게임이 로딩될 시간을 줍니다.

    # --- 2단계: 게임 종료 감지 및 다음 게임 자동 시작 반복 ---
    while True:
        try:
            # 'new_game_button.png'가 나타나면 게임이 끝난 것이므로,
            # 클릭해서 바로 다음 게임을 시작합니다.
            if find_and_click('new_game_button.png', confidence=0.9):
                print("게임 종료를 감지하고, 다음 게임을 바로 시작했습니다.")
                # 다음 게임 화면이 로딩되고, 동일한 버튼을 연속으로 클릭하는 것을 방지하기 위해
                # 클릭 후에는 조금 더 긴 시간(30초)을 대기합니다.
                time.sleep(30) 
            else:
                # 'new_game_button'을 찾지 못하면 게임이 아직 진행 중인 것이므로,
                # 10초 후에 다시 화면을 탐색합니다.
                time.sleep(10)

        except KeyboardInterrupt:
            print("프로그램을 종료합니다.")
            break
        except Exception as e:
            print(f"예상치 못한 오류가 발생했습니다: {e}")
            time.sleep(10)

if __name__ == "__main__":
    main()
