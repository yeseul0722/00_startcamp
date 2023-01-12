# CLI

> GUI와 CLI

- GUI(Graphic User Interface)
  
  -  그래픽을 통해 사용자와 컴퓨터가 상호 작용하는 방식

- CLI(Command Line Interface)
  
  - 명령어를 통해 사용자와 컴퓨터가 상호 작용하는 방식

> Why CLI

- GUI는 CLI에 비해 사용하기 쉽지만 단계가 많고 컴퓨터의 성능을 더 많이 소모 (굳이 GUI 안써도 되니깐)

- 수 많은 서버/ 개발 시스템이 CLI를 통한 조작 환경을 제공

> 기본적인 명령어

- touch
  
  - 파일을 생성하는 명령어

- Mkdir
  
  - 새 폴더를 생성하는 명령어

- Is (list)
  
  - 현재 작업 중인 디렉토리의 폴더/파일 목록을 보여주는 명령어

- cd (change directory)
  
  - 현재 작업 중인 디렉토리를 변경하는 명령어

- start,open
  
  - 폴더/파일을 여는 명령어(Windows에서는 start를, Mac에서는 open 사용)

- .. pwd 
  
  - 현재 파일 위치

- tab
  
  - 자동완성(markdown이면 m치고 tab)

- cd ..
  
  - 파일 뒤로가기

- mv 
  
  - 움직이기

- rm
  
  - 파일을 삭제하는 명령어
  
  - rm -r 는 파일을 지울 수 있음

> 절대경로 vs 상대경로

- 절대 경로
  
  - 루트 디렉토리부터 목적 지점까지 거치는 모든 경로를 전부 작성한 것 
  
  - 윈도우 바탕 화면의 절대 경로 - C:Users/ssafy/Desktop

- 상대 경로
  
  - 현재 작업하고 있는 디렉토리를 기준으로 계산된  상대적 위치를 작성한 것 
  
  - 현재 작업하고 있는 디렉토리가 C:/Users일 때
    윈도우 바탕 화면으로의 상대 경로는 ssafy/Desktop
  
  - ./ : 현재 작업하고 있는 폴더
  
  - ../ : 현재 작업하고 있는 폴더의 부모 폴더
