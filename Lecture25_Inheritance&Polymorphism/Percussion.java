/*
ABSTRACT CLASS PERCUSSION
we want to have this class for inheritance purposes
(to create a hierarchy)
but we do not want to be able to instanciate it
(create an object of class Percussion)
*/

public abstract class Percussion extends Instrument{

  public Percussion(){
    super();
  }

  public Percussion(String n, String o, double pr){
    super(n,o,pr);
  }

  public String toString(){
    String s = "";
    s += "Part of the percussion family! \n";
    s += super.toString();
    return s;
  }
  
  // public abstract void play();  // optional bc percussion is also abstract 
  
}