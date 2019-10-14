class Pixel{
  int x, y; //location
  int w, h; //width and height

  Pixel(int _x, int _y, int _w, int _h){
    x = _x;
    y = _y;
    w = _w;
    h = _h;
  } 

  void display(int _f){
    noStroke();
    fill(_f);
    rect(x,y,w,h); 
  }
}
