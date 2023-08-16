int varY = 0;
int varX = 1600/2;
int velocidade = 5;

void setup(){
  size(1600,900);

}

void draw(){
  frameRate(120);
  background(100);
  varY= varY + velocidade;
  varX+= (velocidade- 3);
  
  
  
  fill(255, 0, 0, 100);
  circle(velocidade+varX, velocidade+varY, 190);
  
  
  fill(0, 0, 255, 100);
  square(100, 100, 100);
  
  
}
