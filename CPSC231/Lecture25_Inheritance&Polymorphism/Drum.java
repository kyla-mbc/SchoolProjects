/*
Drum: which will extend from Instrument
and has a number of pieces.
*/
public class Drum extends Instrument1{

    // member vars
    protected int m_pieces;
  
    // default constructor
    public Drum(){
      super();
      m_pieces = 1;
    }
  
    // fully specified constructor
    public Drum(int pc, String name, String origin, double price){
      super(name, origin, price);
      m_pieces = pc;
    }

    public Drum(Drum d){
      super(d);
      m_pieces = d.m_pieces;
    }
  
    // to string method
    public String toString(){ //overridden
      String s = "";
      s += super.toString();
      s += "The number of pieces is: " + m_pieces;
      return s;
    }
    
    @Override
    public boolean equals(Object o){
      if ((o instanceof Drum) && super.equals(o)){
         Drum d = (Drum) o;
         return this.m_pieces == d.m_pieces;
      } else {
         return false; 
      }
    }
  
    // accecssor
    public int getPieces(){
      return m_pieces;
    }
  
    public void play(){
      System.out.println("!!!BANNNG!!!");
    }
  
  }