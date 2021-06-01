function startDictation()
{
    if (window.hasOwnProperty('webkitSpeechRecognition'))
    {
  
        var recognition = new webkitSpeechRecognition();
  
        recognition.continuous = false;
        recognition.interimResults = false;
  
        recognition.lang = "en-US";
        recognition.start();
        
        recognition.onresult = function(e)
        {   
            var txt = e.results[0][0].transcript;
            document.getElementById('user-transcript').value = txt;
            recognition.stop();
            //document.getElementById('msg').submit();
            if(txt=="burgers")
            {   
                console.log("worked");
                document.getElementById("Burgers").scrollIntoView();
                
            }
            
        };
  
        recognition.onerror = function(e) {
          recognition.stop();
        }
    } 
}
var order={};

function addItem(item, value)
{   
    for(var key in order)
    {   
        if(key===item)
        {  
            var val=order[key];
            order[key]=val+val;
        }
        else
        {   
            
            order[item]=value;
        }
    }
    if(Object.keys(order).length === 0)
    {
        order[item]=value; 
    }
    console.log(order);
}

function speakItem(name)
{   
    if (window.hasOwnProperty('speechSynthesis'))
    {
        var msg = new SpeechSynthesisUtterance();
        msg.lang = 'en';
        msg.text = "one order of "+name;
        window.speechSynthesis.speak(msg); 
        document.getElementById('nyew-transcript').value = msg.text;
    } 
    else
    {
        alert("Sorry, your browser doesn't support text to speech!");
    }
    
}

