public abstract class Instrument1 {
    // all Instrument1s will have these properties:
    // use protected access specifier to allow for inheritance
   protected String m_name;
   protected String m_origin; 
   protected double m_price; 

   // default 
   public Instrument1(){
    m_name = ""; 
    m_origin = null; 
    m_price = -1.0; 
   }

   public Instrument1 (String n, String o, double p){
    m_name = n;
    m_origin = o;
    m_price = p;
   }

   public Instrument1 (Instrument1 i){
    m_name = i.m_name;
    m_origin = i.m_origin;
    m_price = i.m_price;
   }

   public String getName(){
    return m_name;
   }

   public String getOrigin(){
    return m_origin;
   }

   public double getPrice(){
    return m_price;
   }
   /**
    * to Override a method means to give a new implementation to an inherited method. 
    *   - will have the same exact method signature in the parent and 
    *      child classes but with different implementations.
    *   - overriding happens in the context of inheritance
    *   - happens in herachies of classes. 
    * 
    * OVERLOADED - overloaded methods/constructors are multiple methods within the same class
    *               with the same signature but different parameters (number/type)
    */


   @Override // overriding Object class's toString method which only returns memory address
   // to override is to give the a new definition to same process. 
   public String toString(){
        String s = "";
        s += "This object is an Instrument1: " + "\n";
        s += "\tName: " + m_name + "\n";
        s += "\tOrigin: " + m_origin + "\n";
        s += "\tPrice: " + m_price + "\n";
        return s;
   }
   @Override // optional, but override is used for toString and equals 
   public boolean equals (Object o){
        if (this == o){
            return true;
        }
        if (!(o instanceof Instrument1)){
            return false; 
        }
        Instrument1 i = (Instrument1) o;
        return this.m_name.equals(i.m_name);
   }
}

    public abstract void play();
    /**
     * ABTRACT METHOD
     * created when we want all of our non-abstract children to have this method
     * but we don't know what the implementation should look like at this level
     * 
     * makes it so that if a class wants to be an Instrument they MUST 
     * implement a method with this same exact method signature (minus the abstract keyword)
     * or else it will be a syntax error
     * 
     * abstract methods can only exist in abstract classes
     * but abstract classes can have a mix of abstract and non-abstract methods
     */