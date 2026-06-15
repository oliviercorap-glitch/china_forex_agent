2026-06-15T13:46:53.2800476Z Current runner version: '2.335.1'
2026-06-15T13:46:53.2828955Z ##[group]Runner Image Provisioner
2026-06-15T13:46:53.2829951Z Hosted Compute Agent
2026-06-15T13:46:53.2830585Z Version: 20260527.539
2026-06-15T13:46:53.2831251Z Commit: a891dd388383b896fa6ac04a82c0b75cec981078
2026-06-15T13:46:53.2832039Z Build Date: 2026-05-27T21:39:57Z
2026-06-15T13:46:53.2832972Z Worker ID: {1e18555e-96e6-4701-864d-6ac44b67dc73}
2026-06-15T13:46:53.2833765Z Azure Region: northcentralus
2026-06-15T13:46:53.2834517Z ##[endgroup]
2026-06-15T13:46:53.2836440Z ##[group]Operating System
2026-06-15T13:46:53.2837200Z Ubuntu
2026-06-15T13:46:53.2837742Z 24.04.4
2026-06-15T13:46:53.2838287Z LTS
2026-06-15T13:46:53.2838880Z ##[endgroup]
2026-06-15T13:46:53.2839450Z ##[group]Runner Image
2026-06-15T13:46:53.2840154Z Image: ubuntu-24.04
2026-06-15T13:46:53.2840746Z Version: 20260607.184.1
2026-06-15T13:46:53.2842101Z Included Software: https://github.com/actions/runner-images/blob/ubuntu24/20260607.184/images/ubuntu/Ubuntu2404-Readme.md
2026-06-15T13:46:53.2843876Z Image Release: https://github.com/actions/runner-images/releases/tag/ubuntu24%2F20260607.184
2026-06-15T13:46:53.2844916Z ##[endgroup]
2026-06-15T13:46:53.2846048Z ##[group]GITHUB_TOKEN Permissions
2026-06-15T13:46:53.2848714Z Contents: read
2026-06-15T13:46:53.2849358Z Metadata: read
2026-06-15T13:46:53.2849920Z ##[endgroup]
2026-06-15T13:46:53.2852245Z Secret source: Actions
2026-06-15T13:46:53.2853602Z Prepare workflow directory
2026-06-15T13:46:53.3875317Z Prepare all required actions
2026-06-15T13:46:53.3916413Z Getting action download info
2026-06-15T13:46:53.9516173Z Download action repository 'actions/checkout@v4' (SHA:34e114876b0b11c390a56381ad16ebd13914f8d5)
2026-06-15T13:46:54.0312114Z Download action repository 'actions/cache@v3' (SHA:6f8efc29b200d32929f49075959781ed54ec270c)
2026-06-15T13:46:54.1487817Z Download action repository 'actions/setup-python@v5' (SHA:a26af69be951a213d495a4c3e4e4022e16d87065)
2026-06-15T13:46:54.2258002Z Download action repository 'actions/upload-artifact@v4' (SHA:ea165f8d65b6e75b540449e92b4886f43607fa02)
2026-06-15T13:46:54.4634491Z Complete job name: forex-veille
2026-06-15T13:46:54.5466542Z ##[group]Run actions/checkout@v4
2026-06-15T13:46:54.5467656Z with:
2026-06-15T13:46:54.5468298Z   repository: oliviercorap-glitch/china_forex_agent
2026-06-15T13:46:54.5473226Z   token: ***
2026-06-15T13:46:54.5473770Z   ssh-strict: true
2026-06-15T13:46:54.5474293Z   ssh-user: git
2026-06-15T13:46:54.5474836Z   persist-credentials: true
2026-06-15T13:46:54.5475421Z   clean: true
2026-06-15T13:46:54.5475949Z   sparse-checkout-cone-mode: true
2026-06-15T13:46:54.5476555Z   fetch-depth: 1
2026-06-15T13:46:54.5477107Z   fetch-tags: false
2026-06-15T13:46:54.5477633Z   show-progress: true
2026-06-15T13:46:54.5478163Z   lfs: false
2026-06-15T13:46:54.5478670Z   submodules: false
2026-06-15T13:46:54.5479200Z   set-safe-directory: true
2026-06-15T13:46:54.5480162Z ##[endgroup]
2026-06-15T13:46:54.6672946Z Syncing repository: oliviercorap-glitch/china_forex_agent
2026-06-15T13:46:54.6675203Z ##[group]Getting Git version info
2026-06-15T13:46:54.6676170Z Working directory is '/home/runner/work/china_forex_agent/china_forex_agent'
2026-06-15T13:46:54.6677675Z [command]/usr/bin/git version
2026-06-15T13:46:54.6766825Z git version 2.54.0
2026-06-15T13:46:54.6795291Z ##[endgroup]
2026-06-15T13:46:54.6813153Z Temporarily overriding HOME='/home/runner/work/_temp/9a93955c-f207-4e3e-a4a8-d5b30cb14031' before making global git config changes
2026-06-15T13:46:54.6815807Z Adding repository directory to the temporary git global config as a safe directory
2026-06-15T13:46:54.6820730Z [command]/usr/bin/git config --global --add safe.directory /home/runner/work/china_forex_agent/china_forex_agent
2026-06-15T13:46:54.6875771Z Deleting the contents of '/home/runner/work/china_forex_agent/china_forex_agent'
2026-06-15T13:46:54.6881389Z ##[group]Initializing the repository
2026-06-15T13:46:54.6887013Z [command]/usr/bin/git init /home/runner/work/china_forex_agent/china_forex_agent
2026-06-15T13:46:54.7006139Z hint: Using 'master' as the name for the initial branch. This default branch name
2026-06-15T13:46:54.7008473Z hint: will change to "main" in Git 3.0. To configure the initial branch name
2026-06-15T13:46:54.7010729Z hint: to use in all of your new repositories, which will suppress this warning,
2026-06-15T13:46:54.7012440Z hint: call:
2026-06-15T13:46:54.7013613Z hint:
2026-06-15T13:46:54.7014838Z hint: 	git config --global init.defaultBranch <name>
2026-06-15T13:46:54.7016047Z hint:
2026-06-15T13:46:54.7017373Z hint: Names commonly chosen instead of 'master' are 'main', 'trunk' and
2026-06-15T13:46:54.7019253Z hint: 'development'. The just-created branch can be renamed via this command:
2026-06-15T13:46:54.7020831Z hint:
2026-06-15T13:46:54.7021751Z hint: 	git branch -m <name>
2026-06-15T13:46:54.7023086Z hint:
2026-06-15T13:46:54.7024381Z hint: Disable this message with "git config set advice.defaultBranchName false"
2026-06-15T13:46:54.7026805Z Initialized empty Git repository in /home/runner/work/china_forex_agent/china_forex_agent/.git/
2026-06-15T13:46:54.7030944Z [command]/usr/bin/git remote add origin https://github.com/oliviercorap-glitch/china_forex_agent
2026-06-15T13:46:54.7073923Z ##[endgroup]
2026-06-15T13:46:54.7075348Z ##[group]Disabling automatic garbage collection
2026-06-15T13:46:54.7079301Z [command]/usr/bin/git config --local gc.auto 0
2026-06-15T13:46:54.7189001Z ##[endgroup]
2026-06-15T13:46:54.7191601Z ##[group]Setting up auth
2026-06-15T13:46:54.7193490Z [command]/usr/bin/git config --local --name-only --get-regexp core\.sshCommand
2026-06-15T13:46:54.7196982Z [command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'core\.sshCommand' && git config --local --unset-all 'core.sshCommand' || :"
2026-06-15T13:46:54.7504350Z [command]/usr/bin/git config --local --name-only --get-regexp http\.https\:\/\/github\.com\/\.extraheader
2026-06-15T13:46:54.7536873Z [command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'http\.https\:\/\/github\.com\/\.extraheader' && git config --local --unset-all 'http.https://github.com/.extraheader' || :"
2026-06-15T13:46:54.7759219Z [command]/usr/bin/git config --local --name-only --get-regexp ^includeIf\.gitdir:
2026-06-15T13:46:54.7791042Z [command]/usr/bin/git submodule foreach --recursive git config --local --show-origin --name-only --get-regexp remote.origin.url
2026-06-15T13:46:54.8028283Z [command]/usr/bin/git config --local http.https://github.com/.extraheader AUTHORIZATION: basic ***
2026-06-15T13:46:54.8066796Z ##[endgroup]
2026-06-15T13:46:54.8075615Z ##[group]Fetching the repository
2026-06-15T13:46:54.8077223Z [command]/usr/bin/git -c protocol.version=2 fetch --no-tags --prune --no-recurse-submodules --depth=1 origin +1c01d36b1df7ffd0dbd3e7107b2098e5a335b0fe:refs/remotes/origin/main
2026-06-15T13:46:55.1805653Z From https://github.com/oliviercorap-glitch/china_forex_agent
2026-06-15T13:46:55.1807213Z  * [new ref]         1c01d36b1df7ffd0dbd3e7107b2098e5a335b0fe -> origin/main
2026-06-15T13:46:55.1852005Z ##[endgroup]
2026-06-15T13:46:55.1853796Z ##[group]Determining the checkout info
2026-06-15T13:46:55.1855391Z ##[endgroup]
2026-06-15T13:46:55.1859930Z [command]/usr/bin/git sparse-checkout disable
2026-06-15T13:46:55.1908919Z [command]/usr/bin/git config --local --unset-all extensions.worktreeConfig
2026-06-15T13:46:55.1936659Z ##[group]Checking out the ref
2026-06-15T13:46:55.1940200Z [command]/usr/bin/git checkout --progress --force -B main refs/remotes/origin/main
2026-06-15T13:46:55.1986257Z Switched to a new branch 'main'
2026-06-15T13:46:55.1989500Z branch 'main' set up to track 'origin/main'.
2026-06-15T13:46:55.1997316Z ##[endgroup]
2026-06-15T13:46:55.2036390Z [command]/usr/bin/git log -1 --format=%H
2026-06-15T13:46:55.2059081Z 1c01d36b1df7ffd0dbd3e7107b2098e5a335b0fe
2026-06-15T13:46:55.2355139Z ##[group]Run actions/cache@v3
2026-06-15T13:46:55.2356197Z with:
2026-06-15T13:46:55.2357046Z   path: forex_history.json
2026-06-15T13:46:55.2358220Z   key: forex-history-27550742988
2026-06-15T13:46:55.2359195Z   restore-keys: forex-history-

2026-06-15T13:46:55.2360132Z   enableCrossOsArchive: false
2026-06-15T13:46:55.2361042Z   fail-on-cache-miss: false
2026-06-15T13:46:55.2361906Z   lookup-only: false
2026-06-15T13:46:55.2362964Z ##[endgroup]
2026-06-15T13:46:55.5551144Z Cache hit for restore-key: forex-history-27550410728
2026-06-15T13:46:55.7253104Z Received 295 of 295 (100.0%), 0.0 MBs/sec
2026-06-15T13:46:55.7255113Z Cache Size: ~0 MB (295 B)
2026-06-15T13:46:55.7295440Z [command]/usr/bin/tar -xf /home/runner/work/_temp/2537b8d6-580c-45f4-b981-95a53519f910/cache.tzst -P -C /home/runner/work/china_forex_agent/china_forex_agent --use-compress-program unzstd
2026-06-15T13:46:55.7371710Z Cache restored successfully
2026-06-15T13:46:55.7455883Z Cache restored from key: forex-history-27550410728
2026-06-15T13:46:55.7613353Z ##[group]Run actions/cache@v3
2026-06-15T13:46:55.7614367Z with:
2026-06-15T13:46:55.7615127Z   path: pboc_history.json
2026-06-15T13:46:55.7616017Z   key: pboc-history-27550742988
2026-06-15T13:46:55.7616920Z   restore-keys: pboc-history-

2026-06-15T13:46:55.7617829Z   enableCrossOsArchive: false
2026-06-15T13:46:55.7618709Z   fail-on-cache-miss: false
2026-06-15T13:46:55.7619552Z   lookup-only: false
2026-06-15T13:46:55.7620356Z ##[endgroup]
2026-06-15T13:46:56.0920681Z Cache not found for input keys: pboc-history-27550742988, pboc-history-
2026-06-15T13:46:56.1107652Z ##[group]Run actions/setup-python@v5
2026-06-15T13:46:56.1108631Z with:
2026-06-15T13:46:56.1109375Z   python-version: 3.11
2026-06-15T13:46:56.1110205Z   check-latest: false
2026-06-15T13:46:56.1115751Z   token: ***
2026-06-15T13:46:56.1116548Z   update-environment: true
2026-06-15T13:46:56.1117450Z   allow-prereleases: false
2026-06-15T13:46:56.1118293Z   freethreaded: false
2026-06-15T13:46:56.1119075Z ##[endgroup]
2026-06-15T13:46:56.2859023Z ##[group]Installed versions
2026-06-15T13:46:56.2989717Z Successfully set up CPython (3.11.15)
2026-06-15T13:46:56.2994011Z ##[endgroup]
2026-06-15T13:46:56.3139414Z ##[group]Run pip install akshare requests anthropic python-dotenv
2026-06-15T13:46:56.3140873Z [36;1mpip install akshare requests anthropic python-dotenv[0m
2026-06-15T13:46:56.3342256Z shell: /usr/bin/bash -e {0}
2026-06-15T13:46:56.3343562Z env:
2026-06-15T13:46:56.3344476Z   pythonLocation: /opt/hostedtoolcache/Python/3.11.15/x64
2026-06-15T13:46:56.3345831Z   PKG_CONFIG_PATH: /opt/hostedtoolcache/Python/3.11.15/x64/lib/pkgconfig
2026-06-15T13:46:56.3347179Z   Python_ROOT_DIR: /opt/hostedtoolcache/Python/3.11.15/x64
2026-06-15T13:46:56.3348418Z   Python2_ROOT_DIR: /opt/hostedtoolcache/Python/3.11.15/x64
2026-06-15T13:46:56.3349657Z   Python3_ROOT_DIR: /opt/hostedtoolcache/Python/3.11.15/x64
2026-06-15T13:46:56.3350919Z   LD_LIBRARY_PATH: /opt/hostedtoolcache/Python/3.11.15/x64/lib
2026-06-15T13:46:56.3352030Z ##[endgroup]
2026-06-15T13:46:57.3500496Z Collecting akshare
2026-06-15T13:46:57.4131602Z   Downloading akshare-1.18.64-py3-none-any.whl.metadata (13 kB)
2026-06-15T13:46:57.4476993Z Collecting requests
2026-06-15T13:46:57.4526294Z   Downloading requests-2.34.2-py3-none-any.whl.metadata (4.8 kB)
2026-06-15T13:46:57.4994638Z Collecting anthropic
2026-06-15T13:46:57.5036924Z   Downloading anthropic-0.109.1-py3-none-any.whl.metadata (3.2 kB)
2026-06-15T13:46:57.5205832Z Collecting python-dotenv
2026-06-15T13:46:57.5244539Z   Downloading python_dotenv-1.2.2-py3-none-any.whl.metadata (27 kB)
2026-06-15T13:46:57.5429121Z Collecting beautifulsoup4>=4.9.1 (from akshare)
2026-06-15T13:46:57.5467638Z   Downloading beautifulsoup4-4.15.0-py3-none-any.whl.metadata (3.8 kB)
2026-06-15T13:46:57.7428372Z Collecting lxml>=4.2.1 (from akshare)
2026-06-15T13:46:57.7468840Z   Downloading lxml-6.1.1-cp311-cp311-manylinux_2_26_x86_64.manylinux_2_28_x86_64.whl.metadata (3.5 kB)
2026-06-15T13:46:57.8532919Z Collecting pandas>=2.0.0 (from akshare)
2026-06-15T13:46:57.8573341Z   Downloading pandas-3.0.3-cp311-cp311-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl.metadata (79 kB)
2026-06-15T13:46:57.9387449Z Collecting curl_cffi>=0.13.0 (from akshare)
2026-06-15T13:46:57.9429734Z   Downloading curl_cffi-0.15.0-cp310-abi3-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata (18 kB)
2026-06-15T13:46:57.9577992Z Collecting html5lib>=1.0.1 (from akshare)
2026-06-15T13:46:57.9616959Z   Downloading html5lib-1.1-py2.py3-none-any.whl.metadata (16 kB)
2026-06-15T13:46:57.9783568Z Collecting xlrd>=1.2.0 (from akshare)
2026-06-15T13:46:57.9822595Z   Downloading xlrd-2.0.2-py2.py3-none-any.whl.metadata (3.5 kB)
2026-06-15T13:46:58.0029005Z Collecting urllib3>=1.25.8 (from akshare)
2026-06-15T13:46:58.0071563Z   Downloading urllib3-2.7.0-py3-none-any.whl.metadata (6.9 kB)
2026-06-15T13:46:58.0637391Z Collecting tqdm>=4.43.0 (from akshare)
2026-06-15T13:46:58.0681269Z   Downloading tqdm-4.68.2-py3-none-any.whl.metadata (58 kB)
2026-06-15T13:46:58.0884525Z Collecting openpyxl>=3.0.3 (from akshare)
2026-06-15T13:46:58.0928801Z   Downloading openpyxl-3.1.5-py2.py3-none-any.whl.metadata (2.5 kB)
2026-06-15T13:46:58.1054766Z Collecting jsonpath>=0.82 (from akshare)
2026-06-15T13:46:58.1094255Z   Downloading jsonpath-0.82.2.tar.gz (10 kB)
2026-06-15T13:46:58.1195294Z   Installing build dependencies: started
2026-06-15T13:46:58.8647923Z   Installing build dependencies: finished with status 'done'
2026-06-15T13:46:58.8655567Z   Getting requirements to build wheel: started
2026-06-15T13:46:59.2230133Z   Getting requirements to build wheel: finished with status 'done'
2026-06-15T13:46:59.2239145Z   Preparing metadata (pyproject.toml): started
2026-06-15T13:46:59.3916694Z   Preparing metadata (pyproject.toml): finished with status 'done'
2026-06-15T13:46:59.4017175Z Collecting tabulate>=0.8.6 (from akshare)
2026-06-15T13:46:59.4054712Z   Downloading tabulate-0.10.0-py3-none-any.whl.metadata (40 kB)
2026-06-15T13:46:59.4206426Z Collecting decorator>=4.4.2 (from akshare)
2026-06-15T13:46:59.4244602Z   Downloading decorator-5.3.1-py3-none-any.whl.metadata (3.9 kB)
2026-06-15T13:46:59.4465579Z Collecting py-mini-racer>=0.6.0 (from akshare)
2026-06-15T13:46:59.4504873Z   Downloading py_mini_racer-0.6.0-py2.py3-none-manylinux1_x86_64.whl.metadata (8.7 kB)
2026-06-15T13:46:59.4615683Z Collecting akracer>=0.0.13 (from akshare)
2026-06-15T13:46:59.4651892Z   Downloading akracer-0.0.14-py3-none-any.whl.metadata (3.3 kB)
2026-06-15T13:46:59.5501225Z Collecting charset_normalizer<4,>=2 (from requests)
2026-06-15T13:46:59.5541586Z   Downloading charset_normalizer-3.4.7-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (40 kB)
2026-06-15T13:46:59.5701840Z Collecting idna<4,>=2.5 (from requests)
2026-06-15T13:46:59.5739359Z   Downloading idna-3.18-py3-none-any.whl.metadata (6.1 kB)
2026-06-15T13:46:59.5927652Z Collecting certifi>=2023.5.7 (from requests)
2026-06-15T13:46:59.5965668Z   Downloading certifi-2026.5.20-py3-none-any.whl.metadata (2.5 kB)
2026-06-15T13:46:59.6166990Z Collecting anyio<5,>=3.5.0 (from anthropic)
2026-06-15T13:46:59.6206941Z   Downloading anyio-4.13.0-py3-none-any.whl.metadata (4.5 kB)
2026-06-15T13:46:59.6322975Z Collecting distro<2,>=1.7.0 (from anthropic)
2026-06-15T13:46:59.6359358Z   Downloading distro-1.9.0-py3-none-any.whl.metadata (6.8 kB)
2026-06-15T13:46:59.6470635Z Collecting docstring-parser<1,>=0.15 (from anthropic)
2026-06-15T13:46:59.6511669Z   Downloading docstring_parser-0.18.0-py3-none-any.whl.metadata (3.5 kB)
2026-06-15T13:46:59.6671659Z Collecting httpx<1,>=0.25.0 (from anthropic)
2026-06-15T13:46:59.6710317Z   Downloading httpx-0.28.1-py3-none-any.whl.metadata (7.1 kB)
2026-06-15T13:46:59.7496465Z Collecting jiter<1,>=0.4.0 (from anthropic)
2026-06-15T13:46:59.7536967Z   Downloading jiter-0.15.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (5.2 kB)
2026-06-15T13:46:59.8523798Z Collecting pydantic<3,>=1.9.0 (from anthropic)
2026-06-15T13:46:59.8572998Z   Downloading pydantic-2.13.4-py3-none-any.whl.metadata (109 kB)
2026-06-15T13:46:59.8716534Z Collecting sniffio (from anthropic)
2026-06-15T13:46:59.8753197Z   Downloading sniffio-1.3.1-py3-none-any.whl.metadata (3.9 kB)
2026-06-15T13:46:59.8901581Z Collecting typing-extensions<5,>=4.14 (from anthropic)
2026-06-15T13:46:59.8939684Z   Downloading typing_extensions-4.15.0-py3-none-any.whl.metadata (3.3 kB)
2026-06-15T13:46:59.9131277Z Collecting httpcore==1.* (from httpx<1,>=0.25.0->anthropic)
2026-06-15T13:46:59.9167853Z   Downloading httpcore-1.0.9-py3-none-any.whl.metadata (21 kB)
2026-06-15T13:46:59.9298217Z Collecting h11>=0.16 (from httpcore==1.*->httpx<1,>=0.25.0->anthropic)
2026-06-15T13:46:59.9334108Z   Downloading h11-0.16.0-py3-none-any.whl.metadata (8.3 kB)
2026-06-15T13:46:59.9450545Z Collecting annotated-types>=0.6.0 (from pydantic<3,>=1.9.0->anthropic)
2026-06-15T13:46:59.9486757Z   Downloading annotated_types-0.7.0-py3-none-any.whl.metadata (15 kB)
2026-06-15T13:47:00.6002141Z Collecting pydantic-core==2.46.4 (from pydantic<3,>=1.9.0->anthropic)
2026-06-15T13:47:00.6044273Z   Downloading pydantic_core-2.46.4-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (6.6 kB)
2026-06-15T13:47:00.6163136Z Collecting typing-inspection>=0.4.2 (from pydantic<3,>=1.9.0->anthropic)
2026-06-15T13:47:00.6203412Z   Downloading typing_inspection-0.4.2-py3-none-any.whl.metadata (2.6 kB)
2026-06-15T13:47:00.6394114Z Collecting soupsieve>=1.6.1 (from beautifulsoup4>=4.9.1->akshare)
2026-06-15T13:47:00.6434841Z   Downloading soupsieve-2.8.4-py3-none-any.whl.metadata (4.6 kB)
2026-06-15T13:47:00.7333236Z Collecting cffi>=2.0.0 (from curl_cffi>=0.13.0->akshare)
2026-06-15T13:47:00.7373123Z   Downloading cffi-2.0.0-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata (2.6 kB)
2026-06-15T13:47:00.7708841Z Collecting rich (from curl_cffi>=0.13.0->akshare)
2026-06-15T13:47:00.7747928Z   Downloading rich-15.0.0-py3-none-any.whl.metadata (18 kB)
2026-06-15T13:47:00.7875709Z Collecting pycparser (from cffi>=2.0.0->curl_cffi>=0.13.0->akshare)
2026-06-15T13:47:00.7912329Z   Downloading pycparser-3.0-py3-none-any.whl.metadata (8.2 kB)
2026-06-15T13:47:00.8048242Z Collecting six>=1.9 (from html5lib>=1.0.1->akshare)
2026-06-15T13:47:00.8083144Z   Downloading six-1.17.0-py2.py3-none-any.whl.metadata (1.7 kB)
2026-06-15T13:47:00.8201294Z Collecting webencodings (from html5lib>=1.0.1->akshare)
2026-06-15T13:47:00.8237651Z   Downloading webencodings-0.5.1-py2.py3-none-any.whl.metadata (2.1 kB)
2026-06-15T13:47:00.8352141Z Collecting et-xmlfile (from openpyxl>=3.0.3->akshare)
2026-06-15T13:47:00.8387721Z   Downloading et_xmlfile-2.0.0-py3-none-any.whl.metadata (2.7 kB)
2026-06-15T13:47:01.0556614Z Collecting numpy>=1.26.0 (from pandas>=2.0.0->akshare)
2026-06-15T13:47:01.0599622Z   Downloading numpy-2.4.6-cp311-cp311-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl.metadata (6.6 kB)
2026-06-15T13:47:01.0729853Z Collecting python-dateutil>=2.8.2 (from pandas>=2.0.0->akshare)
2026-06-15T13:47:01.0766608Z   Downloading python_dateutil-2.9.0.post0-py2.py3-none-any.whl.metadata (8.4 kB)
2026-06-15T13:47:01.0977757Z Collecting markdown-it-py>=2.2.0 (from rich->curl_cffi>=0.13.0->akshare)
2026-06-15T13:47:01.1015377Z   Downloading markdown_it_py-4.2.0-py3-none-any.whl.metadata (7.4 kB)
2026-06-15T13:47:01.1204285Z Collecting pygments<3.0.0,>=2.13.0 (from rich->curl_cffi>=0.13.0->akshare)
2026-06-15T13:47:01.1246322Z   Downloading pygments-2.20.0-py3-none-any.whl.metadata (2.5 kB)
2026-06-15T13:47:01.1355198Z Collecting mdurl~=0.1 (from markdown-it-py>=2.2.0->rich->curl_cffi>=0.13.0->akshare)
2026-06-15T13:47:01.1391270Z   Downloading mdurl-0.1.2-py3-none-any.whl.metadata (1.6 kB)
2026-06-15T13:47:01.1483771Z Downloading akshare-1.18.64-py3-none-any.whl (1.1 MB)
2026-06-15T13:47:01.1602328Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.1/1.1 MB 113.1 MB/s  0:00:00
2026-06-15T13:47:01.1642134Z Downloading requests-2.34.2-py3-none-any.whl (73 kB)
2026-06-15T13:47:01.1703185Z Downloading charset_normalizer-3.4.7-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (214 kB)
2026-06-15T13:47:01.1763579Z Downloading idna-3.18-py3-none-any.whl (65 kB)
2026-06-15T13:47:01.1826121Z Downloading urllib3-2.7.0-py3-none-any.whl (131 kB)
2026-06-15T13:47:01.1884724Z Downloading anthropic-0.109.1-py3-none-any.whl (923 kB)
2026-06-15T13:47:01.1953781Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 923.9/923.9 kB 147.1 MB/s  0:00:00
2026-06-15T13:47:01.1990008Z Downloading anyio-4.13.0-py3-none-any.whl (114 kB)
2026-06-15T13:47:01.2050091Z Downloading distro-1.9.0-py3-none-any.whl (20 kB)
2026-06-15T13:47:01.2105518Z Downloading docstring_parser-0.18.0-py3-none-any.whl (22 kB)
2026-06-15T13:47:01.2166911Z Downloading httpx-0.28.1-py3-none-any.whl (73 kB)
2026-06-15T13:47:01.2225733Z Downloading httpcore-1.0.9-py3-none-any.whl (78 kB)
2026-06-15T13:47:01.2285011Z Downloading jiter-0.15.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (349 kB)
2026-06-15T13:47:01.2349597Z Downloading pydantic-2.13.4-py3-none-any.whl (472 kB)
2026-06-15T13:47:01.2417305Z Downloading pydantic_core-2.46.4-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (2.1 MB)
2026-06-15T13:47:01.2511269Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.1/2.1 MB 262.1 MB/s  0:00:00
2026-06-15T13:47:01.2547679Z Downloading typing_extensions-4.15.0-py3-none-any.whl (44 kB)
2026-06-15T13:47:01.2604854Z Downloading python_dotenv-1.2.2-py3-none-any.whl (22 kB)
2026-06-15T13:47:01.2664454Z Downloading akracer-0.0.14-py3-none-any.whl (10.1 MB)
2026-06-15T13:47:01.3086488Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 10.1/10.1 MB 248.9 MB/s  0:00:00
2026-06-15T13:47:01.3127421Z Downloading annotated_types-0.7.0-py3-none-any.whl (13 kB)
2026-06-15T13:47:01.3192301Z Downloading beautifulsoup4-4.15.0-py3-none-any.whl (109 kB)
2026-06-15T13:47:01.3262289Z Downloading certifi-2026.5.20-py3-none-any.whl (134 kB)
2026-06-15T13:47:01.3332871Z Downloading curl_cffi-0.15.0-cp310-abi3-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (11.1 MB)
2026-06-15T13:47:01.3755426Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 11.1/11.1 MB 273.1 MB/s  0:00:00
2026-06-15T13:47:01.3796644Z Downloading cffi-2.0.0-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (215 kB)
2026-06-15T13:47:01.3861057Z Downloading decorator-5.3.1-py3-none-any.whl (10 kB)
2026-06-15T13:47:01.3917085Z Downloading h11-0.16.0-py3-none-any.whl (37 kB)
2026-06-15T13:47:01.3974471Z Downloading html5lib-1.1-py2.py3-none-any.whl (112 kB)
2026-06-15T13:47:01.4038944Z Downloading lxml-6.1.1-cp311-cp311-manylinux_2_26_x86_64.manylinux_2_28_x86_64.whl (5.2 MB)
2026-06-15T13:47:01.4232358Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 5.2/5.2 MB 291.5 MB/s  0:00:00
2026-06-15T13:47:01.4272601Z Downloading openpyxl-3.1.5-py2.py3-none-any.whl (250 kB)
2026-06-15T13:47:01.4347313Z Downloading pandas-3.0.3-cp311-cp311-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl (11.3 MB)
2026-06-15T13:47:01.4767333Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 11.3/11.3 MB 279.2 MB/s  0:00:00
2026-06-15T13:47:01.4813749Z Downloading numpy-2.4.6-cp311-cp311-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl (16.9 MB)
2026-06-15T13:47:01.5405179Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 16.9/16.9 MB 295.3 MB/s  0:00:00
2026-06-15T13:47:01.5447970Z Downloading py_mini_racer-0.6.0-py2.py3-none-manylinux1_x86_64.whl (5.4 MB)
2026-06-15T13:47:01.5654128Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 5.4/5.4 MB 294.7 MB/s  0:00:00
2026-06-15T13:47:01.5695653Z Downloading python_dateutil-2.9.0.post0-py2.py3-none-any.whl (229 kB)
2026-06-15T13:47:01.5761541Z Downloading six-1.17.0-py2.py3-none-any.whl (11 kB)
2026-06-15T13:47:01.5819512Z Downloading soupsieve-2.8.4-py3-none-any.whl (37 kB)
2026-06-15T13:47:01.5878121Z Downloading tabulate-0.10.0-py3-none-any.whl (39 kB)
2026-06-15T13:47:01.5936118Z Downloading tqdm-4.68.2-py3-none-any.whl (78 kB)
2026-06-15T13:47:01.5999078Z Downloading typing_inspection-0.4.2-py3-none-any.whl (14 kB)
2026-06-15T13:47:01.6056819Z Downloading xlrd-2.0.2-py2.py3-none-any.whl (96 kB)
2026-06-15T13:47:01.6134080Z Downloading et_xmlfile-2.0.0-py3-none-any.whl (18 kB)
2026-06-15T13:47:01.6196329Z Downloading pycparser-3.0-py3-none-any.whl (48 kB)
2026-06-15T13:47:01.6263434Z Downloading rich-15.0.0-py3-none-any.whl (310 kB)
2026-06-15T13:47:01.6342269Z Downloading pygments-2.20.0-py3-none-any.whl (1.2 MB)
2026-06-15T13:47:01.6418206Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.2/1.2 MB 187.5 MB/s  0:00:00
2026-06-15T13:47:01.6459372Z Downloading markdown_it_py-4.2.0-py3-none-any.whl (91 kB)
2026-06-15T13:47:01.6523428Z Downloading mdurl-0.1.2-py3-none-any.whl (10.0 kB)
2026-06-15T13:47:01.6654299Z Downloading sniffio-1.3.1-py3-none-any.whl (10 kB)
2026-06-15T13:47:01.6711951Z Downloading webencodings-0.5.1-py2.py3-none-any.whl (11 kB)
2026-06-15T13:47:01.7725622Z Building wheels for collected packages: jsonpath
2026-06-15T13:47:01.7734728Z   Building wheel for jsonpath (pyproject.toml): started
2026-06-15T13:47:01.9810388Z   Building wheel for jsonpath (pyproject.toml): finished with status 'done'
2026-06-15T13:47:01.9816736Z   Created wheel for jsonpath: filename=jsonpath-0.82.2-py3-none-any.whl size=5666 sha256=63436e824e69d67a4d1c70c1a5604b241f53f6e581fff3ed06e8a68d71c9aab2
2026-06-15T13:47:01.9818281Z   Stored in directory: /home/runner/.cache/pip/wheels/7d/b8/16/48bbd715040679311fa68cb564ad24a97d9a67fea5d4c848c8
2026-06-15T13:47:01.9833909Z Successfully built jsonpath
2026-06-15T13:47:02.0786985Z Installing collected packages: webencodings, py-mini-racer, jsonpath, xlrd, urllib3, typing-extensions, tqdm, tabulate, soupsieve, sniffio, six, python-dotenv, pygments, pycparser, numpy, mdurl, lxml, jiter, idna, h11, et-xmlfile, docstring-parser, distro, decorator, charset_normalizer, certifi, annotated-types, akracer, typing-inspection, requests, python-dateutil, pydantic-core, openpyxl, markdown-it-py, httpcore, html5lib, cffi, beautifulsoup4, anyio, rich, pydantic, pandas, httpx, curl_cffi, anthropic, akshare
2026-06-15T13:47:12.7282116Z 
2026-06-15T13:47:12.7308304Z Successfully installed akracer-0.0.14 akshare-1.18.64 annotated-types-0.7.0 anthropic-0.109.1 anyio-4.13.0 beautifulsoup4-4.15.0 certifi-2026.5.20 cffi-2.0.0 charset_normalizer-3.4.7 curl_cffi-0.15.0 decorator-5.3.1 distro-1.9.0 docstring-parser-0.18.0 et-xmlfile-2.0.0 h11-0.16.0 html5lib-1.1 httpcore-1.0.9 httpx-0.28.1 idna-3.18 jiter-0.15.0 jsonpath-0.82.2 lxml-6.1.1 markdown-it-py-4.2.0 mdurl-0.1.2 numpy-2.4.6 openpyxl-3.1.5 pandas-3.0.3 py-mini-racer-0.6.0 pycparser-3.0 pydantic-2.13.4 pydantic-core-2.46.4 pygments-2.20.0 python-dateutil-2.9.0.post0 python-dotenv-1.2.2 requests-2.34.2 rich-15.0.0 six-1.17.0 sniffio-1.3.1 soupsieve-2.8.4 tabulate-0.10.0 tqdm-4.68.2 typing-extensions-4.15.0 typing-inspection-0.4.2 urllib3-2.7.0 webencodings-0.5.1 xlrd-2.0.2
2026-06-15T13:47:12.9579486Z ##[group]Run python china_forex_agent.py
2026-06-15T13:47:12.9579903Z [36;1mpython china_forex_agent.py[0m
2026-06-15T13:47:12.9613534Z shell: /usr/bin/bash -e {0}
2026-06-15T13:47:12.9613810Z env:
2026-06-15T13:47:12.9614098Z   pythonLocation: /opt/hostedtoolcache/Python/3.11.15/x64
2026-06-15T13:47:12.9614575Z   PKG_CONFIG_PATH: /opt/hostedtoolcache/Python/3.11.15/x64/lib/pkgconfig
2026-06-15T13:47:12.9615039Z   Python_ROOT_DIR: /opt/hostedtoolcache/Python/3.11.15/x64
2026-06-15T13:47:12.9615457Z   Python2_ROOT_DIR: /opt/hostedtoolcache/Python/3.11.15/x64
2026-06-15T13:47:12.9615869Z   Python3_ROOT_DIR: /opt/hostedtoolcache/Python/3.11.15/x64
2026-06-15T13:47:12.9616284Z   LD_LIBRARY_PATH: /opt/hostedtoolcache/Python/3.11.15/x64/lib
2026-06-15T13:47:12.9616978Z   DEEPSEEK_API_KEY: ***
2026-06-15T13:47:12.9617231Z ##[endgroup]
2026-06-15T13:47:14.5634106Z 2026-06-15 13:47:14,562 [INFO] Démarrage de l'agent de veille des taux de change (version enrichie PBOC)
2026-06-15T13:47:14.7959002Z 2026-06-15 13:47:14,795 [INFO] Taux de marché récupérés pour le 2026-06-12
2026-06-15T13:47:18.0475520Z 
2026-06-15T13:47:18.8644507Z   0%|          | 0/4 [00:00<?, ?it/s]
2026-06-15T13:47:19.5648586Z  25%|██▌       | 1/4 [00:00<00:02,  1.22it/s]
2026-06-15T13:47:20.1285841Z  50%|█████     | 2/4 [00:01<00:01,  1.34it/s]
2026-06-15T13:47:20.6074256Z  75%|███████▌  | 3/4 [00:02<00:00,  1.51it/s]
2026-06-15T13:47:20.6075381Z 100%|██████████| 4/4 [00:02<00:00,  1.69it/s]
2026-06-15T13:47:20.6108356Z                                              
2026-06-15T13:47:20.6109218Z 2026-06-15 13:47:20,610 [INFO] PBOC 美元 mid-rate le 2023-03-06: 689.51
2026-06-15T13:47:21.5659904Z 
2026-06-15T13:47:23.1837405Z   0%|          | 0/4 [00:00<?, ?it/s]
2026-06-15T13:47:25.3541875Z  25%|██▌       | 1/4 [00:01<00:04,  1.62s/it]
2026-06-15T13:47:27.5380977Z  50%|█████     | 2/4 [00:03<00:03,  1.94s/it]
2026-06-15T13:47:28.2249637Z  75%|███████▌  | 3/4 [00:05<00:02,  2.05s/it]
2026-06-15T13:47:28.2250447Z 100%|██████████| 4/4 [00:06<00:00,  1.51s/it]
2026-06-15T13:47:28.2270566Z                                              
2026-06-15T13:47:28.2271443Z 2026-06-15 13:47:28,226 [INFO] PBOC 欧元 mid-rate le 2023-03-06: 732.8
2026-06-15T13:47:28.7905190Z 
2026-06-15T13:47:29.7029529Z   0%|          | 0/4 [00:00<?, ?it/s]
2026-06-15T13:47:30.6497308Z  25%|██▌       | 1/4 [00:00<00:02,  1.10it/s]
2026-06-15T13:47:31.2176887Z  50%|█████     | 2/4 [00:01<00:01,  1.07it/s]
2026-06-15T13:47:31.6941946Z  75%|███████▌  | 3/4 [00:02<00:00,  1.31it/s]
2026-06-15T13:47:31.6943298Z 100%|██████████| 4/4 [00:02<00:00,  1.53it/s]
2026-06-15T13:47:31.6963683Z                                              
2026-06-15T13:47:31.6964690Z 2026-06-15 13:47:31,696 [INFO] PBOC 日元 mid-rate le 2023-03-06: 5.0718
2026-06-15T13:47:32.4030867Z 
2026-06-15T13:47:33.1064371Z   0%|          | 0/4 [00:00<?, ?it/s]
2026-06-15T13:47:34.0224541Z  25%|██▌       | 1/4 [00:00<00:02,  1.42it/s]
2026-06-15T13:47:34.7376352Z  50%|█████     | 2/4 [00:01<00:01,  1.21it/s]
2026-06-15T13:47:35.2129350Z  75%|███████▌  | 3/4 [00:02<00:00,  1.29it/s]
2026-06-15T13:47:35.2130408Z 100%|██████████| 4/4 [00:02<00:00,  1.52it/s]
2026-06-15T13:47:35.2151317Z                                              
2026-06-15T13:47:35.2152854Z 2026-06-15 13:47:35,214 [INFO] PBOC 英镑 mid-rate le 2023-03-06: 829.7
2026-06-15T13:47:35.9168239Z 
2026-06-15T13:47:36.6161863Z   0%|          | 0/4 [00:00<?, ?it/s]
2026-06-15T13:47:37.3177262Z  25%|██▌       | 1/4 [00:00<00:02,  1.43it/s]
2026-06-15T13:47:38.0230185Z  50%|█████     | 2/4 [00:01<00:01,  1.43it/s]
2026-06-15T13:47:38.5070456Z  75%|███████▌  | 3/4 [00:02<00:00,  1.42it/s]
2026-06-15T13:47:38.5071041Z 100%|██████████| 4/4 [00:02<00:00,  1.62it/s]
2026-06-15T13:47:38.5090082Z                                              
2026-06-15T13:47:38.5090984Z 2026-06-15 13:47:38,508 [INFO] PBOC 港币 mid-rate le 2023-03-06: 87.837
2026-06-15T13:47:38.5093203Z Traceback (most recent call last):
2026-06-15T13:47:38.5099997Z   File "/home/runner/work/china_forex_agent/china_forex_agent/china_forex_agent.py", line 486, in <module>
2026-06-15T13:47:38.5101017Z     run_forex_agent()
2026-06-15T13:47:38.5102243Z   File "/home/runner/work/china_forex_agent/china_forex_agent/china_forex_agent.py", line 464, in run_forex_agent
2026-06-15T13:47:38.5103358Z     pboc_rates = update_pboc_history()
2026-06-15T13:47:38.5104032Z                  ^^^^^^^^^^^^^^^^^^^^^
2026-06-15T13:47:38.5105323Z   File "/home/runner/work/china_forex_agent/china_forex_agent/china_forex_agent.py", line 213, in update_pboc_history
2026-06-15T13:47:38.5106504Z     save_pboc_history(pboc_history)
2026-06-15T13:47:38.5107688Z   File "/home/runner/work/china_forex_agent/china_forex_agent/china_forex_agent.py", line 182, in save_pboc_history
2026-06-15T13:47:38.5108693Z     json.dump(history, f, indent=2, ensure_ascii=False)
2026-06-15T13:47:38.5109809Z   File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/json/__init__.py", line 179, in dump
2026-06-15T13:47:38.5110581Z     for chunk in iterable:
2026-06-15T13:47:38.5111527Z   File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/json/encoder.py", line 432, in _iterencode
2026-06-15T13:47:38.5112321Z     yield from _iterencode_dict(o, _current_indent_level)
2026-06-15T13:47:38.5113645Z   File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/json/encoder.py", line 406, in _iterencode_dict
2026-06-15T13:47:38.5116007Z     yield from chunks
2026-06-15T13:47:38.5116933Z   File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/json/encoder.py", line 406, in _iterencode_dict
2026-06-15T13:47:38.5117680Z     yield from chunks
2026-06-15T13:47:38.5118216Z   File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/json/encoder.py", line 406, in _iterencode_dict
2026-06-15T13:47:38.5118717Z     yield from chunks
2026-06-15T13:47:38.5119183Z   File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/json/encoder.py", line 439, in _iterencode
2026-06-15T13:47:38.5119670Z     o = _default(o)
2026-06-15T13:47:38.5119891Z         ^^^^^^^^^^^
2026-06-15T13:47:38.5120341Z   File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/json/encoder.py", line 180, in default
2026-06-15T13:47:38.5120935Z     raise TypeError(f'Object of type {o.__class__.__name__} '
2026-06-15T13:47:38.5121337Z TypeError: Object of type date is not JSON serializable
2026-06-15T13:47:38.7381902Z ##[error]Process completed with exit code 1.
2026-06-15T13:47:38.7538941Z Post job cleanup.
2026-06-15T13:47:38.8511916Z [command]/usr/bin/git version
2026-06-15T13:47:38.8549531Z git version 2.54.0
2026-06-15T13:47:38.8596673Z Temporarily overriding HOME='/home/runner/work/_temp/93813762-1219-4860-8bb5-a427c58eced7' before making global git config changes
2026-06-15T13:47:38.8598132Z Adding repository directory to the temporary git global config as a safe directory
2026-06-15T13:47:38.8603328Z [command]/usr/bin/git config --global --add safe.directory /home/runner/work/china_forex_agent/china_forex_agent
2026-06-15T13:47:38.8639681Z [command]/usr/bin/git config --local --name-only --get-regexp core\.sshCommand
2026-06-15T13:47:38.8671537Z [command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'core\.sshCommand' && git config --local --unset-all 'core.sshCommand' || :"
2026-06-15T13:47:38.8896567Z [command]/usr/bin/git config --local --name-only --get-regexp http\.https\:\/\/github\.com\/\.extraheader
2026-06-15T13:47:38.8919818Z http.https://github.com/.extraheader
2026-06-15T13:47:38.8931615Z [command]/usr/bin/git config --local --unset-all http.https://github.com/.extraheader
2026-06-15T13:47:38.8961638Z [command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'http\.https\:\/\/github\.com\/\.extraheader' && git config --local --unset-all 'http.https://github.com/.extraheader' || :"
2026-06-15T13:47:38.9179636Z [command]/usr/bin/git config --local --name-only --get-regexp ^includeIf\.gitdir:
2026-06-15T13:47:38.9209448Z [command]/usr/bin/git submodule foreach --recursive git config --local --show-origin --name-only --get-regexp remote.origin.url
2026-06-15T13:47:38.9547235Z Cleaning up orphan processes
2026-06-15T13:47:38.9825691Z ##[warning]Node.js 20 actions are deprecated. The following actions are running on Node.js 20 and may not work as expected: actions/cache@v3, actions/checkout@v4, actions/setup-python@v5. Actions will be forced to run with Node.js 24 by default starting June 16th, 2026. Node.js 20 will be removed from the runner on September 16th, 2026. Please check if updated versions of these actions are available that support Node.js 24. To opt into Node.js 24 now, set the FORCE_JAVASCRIPT_ACTIONS_TO_NODE24=true environment variable on the runner or in your workflow file. Once Node.js 24 becomes the default, you can temporarily opt out by setting ACTIONS_ALLOW_USE_UNSECURE_NODE_VERSION=true. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/
