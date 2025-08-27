🧪 Selenium 로그인/로그아웃 자동화

 - 이 프로젝트는 Python의 Selenium 라이브러리를 사용하여 'https://the-internet.herokuapp.com/login' 공개용 웹사이트에서 로그인 및 로그아웃 기능을 자동화한 스크립트입니다.<br><br>


✅ 주요 기능
 - 사용자 인증 자동화
 - 로그인 프로세스 실행
 - 성공 Toast 팝업 확인
 - 로그아웃 처리 자동화<br><br>


🛠️ 사용 기술

 - Python v3.13.7  
 - Selenium v4.35.0  
 - ChromeDriver v139.0.7258.128<br><br>



🚀 환경 준비

 - Python(v3.13.7) 설치
 - Selenium(v4.35.0) 설치 ('pip install selenium' 입력)
 - Chrome 브라우저 버전 확인 (Chrome 주소창에 'chrome://version' 입력)
 - ChromeDriver 다운로드 (Chrome 브라우저 버전과 동일한 버전으로 다운로드)
 - ChromeDriver 경로 확인 (ex. 'C:/python/chromedriver-win64')<br><br>



🧭 소스코드 내 경로 설정 확인
 - login_logout.py 파일에서 아래 경로는 본인 PC에 맞게 수정합니다.
 - chrome_driver_path = 'C:/python/chromedriver-win64/chromedriver.exe' (chromedriver.exe 필수 입력)<br><br>



💻스크립트 실행
 - vscode 에디터에서 스크립트가 있는 폴더로 이동 후, 아래 명령어 입력하여 실행합니다.
 - 'python login_logout.py'<br><br>
<img width="1084" height="159" alt="image" src="https://github.com/user-attachments/assets/0bb22a4a-b834-4d93-b415-8ed7d7db8a59"><br><br>



📌 실행 결과
 - Chrome 브라우저가 자동으로 실행되며, 로그인 후 아래와 같은 팝업이 표시됩니다.
<img width="1022" height="783" alt="image" src="https://github.com/user-attachments/assets/f7e1d7e5-e4a7-4c99-b88a-5693cc9f1746"><br><br>
 - 로그인 성공 후, 로그아웃 버튼이 자동으로 클릭되며 로그아웃이 정상적으로 처리됩니다.<br><br>


⚙️동작 흐름
 1. Chrome 브라우저 실행 후, 로그인 페이지 접속 
 2. 사용자 ID,PW 자동으로 입력하여 로그인 시도
 3. 로그인 성공 Toast 팝업 확인
 4. 해당 팝업 닫고, 로그아웃 버튼 클릭
 5. 로그아웃 처리되었는지 확인
 6. Chrome 브라우저 종료<br><br>



📝참고 사항

 - 'time.sleep()' 으로 대기 시간을 주고 있어 네트워크 상황에 따라 수정 가능합니다.
 - 로그인 alert 팝업은 time.sleep(2) 후, 자동으로 닫히도록 설정합니다.<br><br>
