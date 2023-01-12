> Git이란

분산 버전 관리 프로그램

- 버전: 컴퓨터 소프트웨어의 특정 상태

- 관리: 어떤 일의 사무, 시설이나 물건의 유지. 개량

- 프로그램: 컴퓨터에서 실행될 때 특정 작업을 수행하는 일련의 명령어들의 모음

> 버전관리

바뀐 파일을 모두 갖고 있으면 용량이 매우 커짐 -> 

어떤 파일의 어떤 부분이 바꼈는지, 이유 등만 정리를 하고 파일로 저장해놓고,

최종파일은 한개만 남겨두면 용량을 아끼면서 버전 관리를 할 수 있음

>  분산 버전 관리 프로그램

- 코드의 히스토리(버전)을 관리하는 도구

- 개발되어온 과정 파악 가능

- 이전 버전과의 변경 사항 비교 및 분석

- GitLab
  
  - private

- GitHub
  
  - public

> Git이란

Git (분산 버전 관리 프로그램) =/ GitHub (Git 기반의 저장 서비스)

> Repository

특정 디렉토리를 버전 관리하는 저장소

- git init 명령어로 로컬 저장소를 생성

- .git 디렉토리에 버전 관리에 필요한 모든 것이 들어있음

> Git 기본기

- README.md 생성하기
  
  - 새 폴더를 만들고 README.md 파일을 생성해 주세요.
  
  - 이 파일을 버전 관리하며 Git을 사용해 봅시다.
  
  - -> 특정 버전으로 남긴다 = "커밋(Commt)한다"

- Working Directory
  
  - 내가 작업하고 있는 실제 디렉토리

- Staging Area
  
  - 커밋으로 남기고 싶은, 특정 버전으로 관리하고 싶은 파일이 있는 곳

- Repository
  
  - 커밋들이 저장되는 곳

```git
SSAFY@DESKTOP-DOGVPUB MINGW64 ~/Desktop/StartCamp (master)
$ git status
On branch master
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        CLI/

nothing added to commit but untracked files present (use "git add" to track)

SSAFY@DESKTOP-DOGVPUB MINGW64 ~/Desktop/StartCamp (master)
$ touch git.txt // git.txt 파일 생성

SSAFY@DESKTOP-DOGVPUB MINGW64 ~/Desktop/StartCamp (master)
$ git status //git 상태 확인
On branch master
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        CLI/
        git.txt

nothing added to commit but untracked files present (use "git add" to track)

SSAFY@DESKTOP-DOGVPUB MINGW64 ~/Desktop/StartCamp (master)
$ git add git.txt  // staging area로 파일 보내기

SSAFY@DESKTOP-DOGVPUB MINGW64 ~/Desktop/StartCamp (master)
$ git commit -m "Third Class" //-m 메시지 남기기 깃에 커밋하기
[master 91d4eaf] Third Class
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 git.txt

SSAFY@DESKTOP-DOGVPUB MINGW64 ~/Desktop/StartCamp (master)
$ git log //커밋 상태 확
commit 91d4eaf7653a48a73c48c08e56676bfc9317c389 (HEAD -> master)
Author: yeseul0722 <pdy051257@naver.com>
Date:   Wed Jan 11 17:03:23 2023 +0900

    Third Class

commit 5789a30d61e66a709704504c20ee0b8902240ace
Author: yeseul0722 <pdy051257@naver.com>
Date:   Wed Jan 11 16:59:36 2023 +0900

    second Class - cil

commit 447b7019c5067dc1d37de1978d217ce7b18b5995
Author: yeseul0722 <pdy051257@naver.com>
Date:   Wed Jan 11 16:55:45 2023 +0900

    first class 230111| markdown
```

```git
SSAFY@DESKTOP-DOGVPUB MINGW64 ~/Desktop/StartCamp (master)
$ git config --global user.email "pdy051257@naver.com"

SSAFY@DESKTOP-DOGVPUB MINGW64 ~/Desktop/StartCamp (master)
$  git config --global user.name "yeseul0722"
// 계정 정보 등록
```
