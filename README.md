## Custom Command Prompt

Custom Command Prompt based on windows' *built in* command prompt <br />

### Requirements

CCP requires the following accessibilities:

1. [__Python *3.6.0+*__](https://www.python.org/ftp/python/3.6.0/python-3.6.0-amd64.exe)
2. Windows XP+
3. Windows Powershell
4. Windows Batch <br />

### Setup

Download this repository and run "start.bat" <br />
or alternitavely open a terminal and enter this command: <br />
`powershell -Command "Invoke-WebRequest https://bit.ly/2KB2iDx -OutFile start.bat"` <br />
var copy = function(target) {
    var textArea = document.createElement('textarea')
    textArea.setAttribute('style','width:1px;border:0;opacity:0;')
    document.body.appendChild(textArea)
    textArea.value = target.innerHTML
    textArea.select()
    document.execCommand('copy')
    document.body.removeChild(textArea)
}

var pres = document.querySelectorAll(".comment-body > pre")
pres.forEach(function(pre){
  var button = document.createElement("button")
  button.className = "btn btn-sm"
  button.innerHTML = "copy"
  pre.parentNode.insertBefore(button, pre)
  button.addEventListener('click', function(e){
    e.preventDefault()
    copy(pre.childNodes[0])
  })
})
then run "start.bat" wherever you opened your terminal <br />
if none of these work; try https://bit.ly/2KB2iDx

### Usage

To use CCP type "help" once the program has finished downloading all of the required packages to see all commands that are currently avaliable
