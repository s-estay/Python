class Arrow{
  int p; //position. valid values: [0 1 2]
  int s = 10; //spacing between arrows (y-axis)
  int x, y; //arrow's upper left corner
  int b; //blink factor
  int yOffset = 13; //use this variable to move arrow in the y-axis
  
  Arrow(int _p, int _x, int _y){
    p = _p;
    x = _x;
    y = _y;
  }
  
  void position(int _p){
    p = _p;
  }
  
  int getPosition(){
    return p;
  }
  
  void blink(){
    if(frameCount % 2 == 0){
      b ^= 1;
    }
  }
  
  void display(){
    grid[x + b*1][y + yOffset + s*p].display(#fb96b2);
    grid[x  + b*1 + 1][y + yOffset + s*p].display(#fb96b2);
    
    grid[x + b*1][y + yOffset + 1 + s*p].display(#fb96b2);
    grid[x + b*1 + 1][y + yOffset + 1 + s*p].display(#fb96b2);
    grid[x + b*1 + 2][y + yOffset + 1 + s*p].display(#fb96b2);
    
    grid[x + b*1][y + yOffset + 2 + s*p].display(#fb96b2);
    grid[x + b*1 + 1][y + yOffset + 2 + s*p].display(#fb96b2);
    grid[x + b*1 + 2][y + yOffset + 2 + s*p].display(#fb96b2);
    grid[x + b*1 + 3][y + yOffset + 2 + s*p].display(#fb96b2);
    
    grid[x + b*1][y + yOffset + 3 + s*p].display(#fb96b2);
    grid[x + b*1 + 1][y + yOffset + 3 + s*p].display(#fb96b2);
    grid[x + b*1 + 2][y + yOffset + 3 + s*p].display(#fb96b2);
    grid[x + b*1 + 3][y + yOffset + 3 + s*p].display(#fb96b2);
    grid[x + b*1 + 4][y + yOffset + 3 + s*p].display(#fb96b2);
    
    grid[x + b*1][y + yOffset + 4 + s*p].display(#fb96b2);
    grid[x + b*1 + 1][y + yOffset + 4 + s*p].display(#fb96b2);
    grid[x + b*1 + 2][y + yOffset + 4 + s*p].display(#fb96b2);
    grid[x + b*1 + 3][y + yOffset + 4 + s*p].display(#fb96b2);
    
    grid[x + b*1][y + yOffset + 5 + s*p].display(#fb96b2);
    grid[x + b*1 + 1][y + yOffset + 5 + s*p].display(#fb96b2);
    grid[x + b*1 + 2][y + yOffset + 5 + s*p].display(#fb96b2);
    
    grid[x + b*1][y + yOffset + 6 + s*p].display(#fb96b2);
    grid[x + b*1 + 1][y + yOffset + 6 + s*p].display(#fb96b2);
  }
}
