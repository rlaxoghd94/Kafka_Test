## Git Branch Naming
--------------------

참고:
- <http://mirocommunity.readthedocs.io/en/latest/internals/branching-model.html> Git Branching naming convention - Eng
- <http://rumblefish.tistory.com/65> Git Branching - Kor
- <https://github.com/Kunena/Kunena-Forum/wiki/Create-a-new-branch-with-git-and-manage-branches> Git CheatSheet

1. 전제 조건
모든 활동은 GitHub에서 제공하는 Issue로 등록한다. hotfix, feature, issure 브랜치는 GitHub에 등록된 <issue_number>를 기준으로 생성한다.

2. GitHub 설정
GitHub에는 master와 develop 브랜치, 그리고 master 브랜치의 TAG만 관리한다.
- GitHub에 새 저장소를 생성한다.
- 기본으로 master 브랜치가 생성된다.
 - 소프트웨어 배포 버전을 관리하며, 배포된 버전의 태그만 부여한다.
 - 태그 명명규칙: REL-X.X
- master 브랜치로부터 develop 브랜치를 생성한다.
 - 개발용 메인 브랜치로 활용한다.

3. 개발자 PC
개발자는 PC에 realease, hotfix, feature, issue 브랜치를 생성하여 작업을 진행한다.
작업이 완료된 브랜치는 병합 후 삭제 가능하며, GitHub에 반영하지 않는다.

4. release 브랜치
- develop 브랜치로부터 생성하는 브랜치이다.
- 명명규칙: release/X.X.X
- 브랜치 생성 후에는 버그픽스만 반영한다.
- 최종 확정 후에는 develop와 master 브랜치에 병합한다.
 - master 브랜치에 병합 후 태그를 부여한다.

5. hotfix 브랜치
master 브랜치로부터 생성하는 브랜치이다.
master 브랜치에 심각한 오류가 있는 경우에만 생성한다.
- 명명규칙: hotfix<issue_number>
- 완료 후 master, release, develop 브랜치에 병합한다.

6. feature 브랜치
- develop 브랜치로부터 생성하는 브랜치이다.
- 명명규칙: feature/<issue_number><짧은설명>
- 완료 후 develop 브랜치에 병합한다.

7. issue 브랜치
- develop, feature, release 브랜치로부터 생성하는 브랜치이다.
- 명명규칙: issue/<issue_number>
- 완료 후에는 생성된 부모 브랜치로 병합한다.
