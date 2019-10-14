import deadpixel.command.*;

PFont f;
int i = 0;
int maxValue = 10;

Pixel[][] grid;
int cols = 64;
int rows = 48;
Arrow arrow = new Arrow(0, 10, 4);
Screen screen = new Screen(0);
 
void setup() {  
  //fullScreen();
  
  
  size(800, 480);
  
  grid = new Pixel[cols][rows];
  for(int i = 0; i < cols; ++i){
    for(int j = 0; j < rows; ++j){
      grid[i][j] = new Pixel(i*10, j*10, 10, 10);
    }
  }
  
  f = createFont("karmatic_arcade.ttf", 100);
  textFont(f);
  textAlign(CENTER);
  //frameRate(2);
  
  //noLoop();
}

void draw(){
  //display();
  //update();
  //pyText();
  //screen.display();
  //pyButton();
}

void keyPressed(){
  if(key == CODED){
    if(keyCode == UP && arrow.getPosition() > 0){
      arrow.position(arrow.getPosition() - 1);
    }
    else if(keyCode == DOWN && arrow.getPosition() < 2){
      arrow.position(arrow.getPosition() + 1);
    }
  }
}
 
void pyButton(){
  String scriptPath = sketchPath("button.py");
  Command script = new Command("python " + scriptPath);
  
  if(script.run() == true){
    String[] output = script.getOutput();
    String s = output[0]; 
    //text(s, width*0.5, height*0.75);
    println(s);
  }
}

void pyText(){
  background(0);
  text("SCORE", width*0.5, height*0.35);
  
  String scriptPath = sketchPath("hello.py");
  Command script = new Command("python " + scriptPath);
  
  if(script.run() == true){
    String[] output = script.getOutput();
    String s = output[0]; 
    text(s, width*0.5, height*0.75);
  }
}

void display(){
  fill(255);
  background(0);
  if(i == 0){
    text("00", width/2, height/2);
  }
  else{
    text(i*10, width/2, height/2);
  }
}

void update(){
  if(i > maxValue -1){
    i = 0;
  }
  else{
    ++i;
  }
}
