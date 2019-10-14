PFont fTitle;
PFont fMenu;

class Screen{
  int s; //screen
  
  Screen(int _s){
    s = _s;
  }
  
  void setScreen(int _s){
    s = _s;
  }
  
  void display(){
    if(s == 0){
      background(#63CBD3);
      fill(0);
      
      fTitle = createFont("karmatic_arcade.ttf", 100);
      textFont(fTitle);
      textAlign(CENTER);
      text("GODISPONG", width/2, 100);
      
      fMenu = createFont("karmatic_arcade.ttf", 75);
      textFont(fMenu);
      textAlign(LEFT);
      text("TIMER", 200, 225);
      text("UTMANING", 200, 325);
      text("EXIT", 200, 425);
      
      arrow.display();
      arrow.blink();
    }
    else if(s == 1){
      background(0);
    }
    else if(s == 2){
      background(255);
    }
  }
}
