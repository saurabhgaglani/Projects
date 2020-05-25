

function faca()
{
    var str=document.getElementById("favchar").value
    document.getElementById("sub").innerHTML=" "+str;

}

function bar()
{
    var val=document.getElementById("myRange").value
    document.getElementById("dem").innerHTML= " The value you entered is- "+val+"\n";
    if(val<=4)
    {
        document.getElementById("dem").innerHTML=" We are sorry you feel this way, give us another chance? :(";

    }
    else if(val==5)
    {
        document.getElementById("dem").innerHTML=" Neutral?Huh? Watch Rapunzel and you won't be ;)";
    }
    else if(val>5 && val<8)
    {
        document.getElementById("dem").innerHTML=" Thats a decent rating, Thank you :)";
    }
    else if(val>=8 && val<=10)
    {
        document.getElementById("dem").innerHTML=" That put a smile on our faces, thank you! :D";
    }
}

function daca()
{
  
    var ran = Math.ceil(Math.random()*4)
    if(ran == 1)
    {
        document.getElementById("im").innerHTML="<img src=\"mm.png\" width=\"220px\" height=\"220px\">"; //https://en.wikipedia.org/wiki/Mickey_Mouse
        

        document.getElementById("hem").innerHTML= "Mickey Mouse!"
        document.getElementById("cem").innerHTML= document.getElementById("cem").innerHTML= "Movie: Mickey Mouse <br><br> Main Rival: None <br><br> Best Friend: Donald Duck <br><br> Song from Movie: Roll call!<br><br> Lyrics from song<br><br> M-I-C-K-E-Y<br>M-O-U-S-E (that's me!) <br>M-I-C-K-E-Y<br>M-O-U-S-E<br>It's the Mickey Mouse Clubhouse <br>Come inside, it's fun inside <br>It's the Mickey Mouse Clubhouse (roll call!)"
    }
    else if(ran == 2)
    {
        document.getElementById("im").innerHTML="<img src=\"lm.png\" width=\"220px\" height=\"220px\">"; //https://en.wikipedia.org/wiki/Lightning_McQueen


    document.getElementById("hem").innerHTML= "Lightning McQueen!"
    document.getElementById("cem").innerHTML= document.getElementById("cem").innerHTML= "Movie: Cars <br><br> Main Rival: Chick Hicks <br><br> Best Friend: Mater <br><br> Song from Movie: Life is a Highway<br><br> Lyrics from song<br><br> Life's like a road that you travel on<br>When there's one day here and the next day gone<br>Sometimes you bend and sometimes you stand<br>Sometimes you turn your back to the wind"
    }
    else if(ran == 3)
    {
        document.getElementById("im").innerHTML="<img src=\"al.png\" width=\"220px\" height=\"220px\">"; //https://en.wikipedia.org/wiki/Aladdin_(Disney_character)


    document.getElementById("hem").innerHTML= "Alladin!"
    document.getElementById("cem").innerHTML= document.getElementById("cem").innerHTML= "Movie: Alladin <br><br> Main Rival: Jaffar <br><br> Best Friend: Abu <br><br> Song from Movie: Arabian Nights <br><br> Lyrics from song<br><br> Venho de um lugar,<br>onde sempre se vê,<br>uma carava passar"
    
    }
    else if(ran == 4)
    {
        document.getElementById("im").innerHTML="<img src=\"pp.jpg\" width=\"220px\" height=\"220px\">"; //https://www.microsoft.com/en-us/p/peter-pan-return-to-neverland/8d6kgwzl5w99?activetab=pivot%3aoverviewtab


    document.getElementById("hem").innerHTML= "Peter Pan!"
    document.getElementById("cem").innerHTML= "Movie: Peter Pan <br><br> Main Rival: Captain Hook <br><br> Best Friend: Tinker Bell <br><br> Song from Movie: You can Fly!<br><br> Lyrics from song<br><br> But, Peter, how do we get to Never Land? Fly, of course!<br>Fly!<br> It's easy! All you have to do is to is to is to <br> Huh That's funny!<br> What's the matter?<br> Don't you know? Don't you know?<br>Oh sure, it's, it's just that I never thought about it before <br>Say, that's it! You think of a wonderful thought! <br>Any happy little thought?<br>Uhhuh<br>Like toys at Christmas? Sleight bells? Snow?<br>Yep! Watch me nowhere I go! <br>It's easier than pie!"
    }
}
