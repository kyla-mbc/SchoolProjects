// Guitar is a derived class from base class Instrument
// aka child class from parent child Instrument

public class Guitar extends Instrument1{ // extend establishes the inheritance 
    protected int m_strings; // number of strings 
  
    public Guitar(){
      // FIRST THING TO DO IN CONSTRUCTORS ALWAYS when we use inheritance
      // is to call the super constructor
      super(); // calls the parent's default constructor (super = parent)
                // somewhat like doing: Instrument(); except this is illegal :) 
      m_strings = 6;
    }
    // overloaded constructor 
    public Guitar(int s){
      super();
      m_strings = s;
    }

    // fully specified 
    public Guitar(int s, String name, String origin, double price){
      super(name, origin, price);
      m_strings = s;
    }
  
    // copy 
    public Guitar(Guitar g){
      super(g); // call the parent's copy constructor 
      m_strings = g.m_strings;
    }
  
    public int getStrings(){
      return m_strings;
    }
  
    @Override
    public String toString(){
      String s = "";
      s += super.toString(); // call the Instument's toString
      s += "The number of strings is:" + m_strings +"\n";
      return s;
    }
    @Override
    public boolean equals(Object o){
      if ((o instanceof Guitar) && super.equals(o)){
         // could return true at this point if we want to just check the name 
         // and that o is a Guitar 
         // or check if the number of strings is equal too
         Guitar g = (Guitar) o;
         return this.m_strings == g.m_strings;
      } else {
         return false; 
      }
    }

    public void play(){
      System.out.println("TWAAANNNGGG!");
    }

  }
  