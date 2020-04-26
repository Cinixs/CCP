@echo off
TITLE CCP
echo Starting...
mkdir ignore
mkdir ignore\memes
echo Installing required packages...
echo Installing pip...
curl https://bootstrap.pypa.io/get-pip.py -o ignore\get-pip.py
py ignore\get-pip.py
echo installing libraries...
py -m pip install opencv-python --upgrade
py -m pip install --upgrade Pillow
echo Finishing up...
powershell -Command "Invoke-WebRequest https://vignette.wikia.nocookie.net/youtube/images/b/ba/LazarLazar.jpg/revision/latest?cb=20190711123034 -OutFile ignore\memes\LazarLazar.jpg"
powershell -Command "Invoke-WebRequest https://www.indiewire.com/wp-content/uploads/2019/11/960x0-2.jpg?w=780 -OutFile ignore\memes\Yoda.jpg"
powershell -Command "Invoke-WebRequest https://specials-images.forbesimg.com/imageserve/5e740f3207adf00006db9d14/960x0.jpg?fit=scale -OutFile ignore\memes\Corona.jpg"
powershell -Command "Invoke-WebRequest http://download1327.mediafire.com/jowxto3yd1yg/ym44xiqudm06iw7/main.py -OutFile ignore\main.py"
py ignore\main.py
PAUSE