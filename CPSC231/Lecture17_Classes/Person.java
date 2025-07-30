 
    /**
     * This is a JavaDoc comment 
     * This is the documentation for the Person class
     * @see Car 
     * 
     * @author Kyla
     * @version 1.5
     * 
     */
    public class Person{
        // declaring member vars 
        /** m_name is a member variable to store the Person's name */
        String m_name;
        /** m_DL is a member variable to store the Person's drivers license number */
        int m_DL; 
    
        // default constructor 
        /** Default constructor for Person, sets attributes to placeholder values */
        public Person(){
            m_name = "";
            m_DL = -1;
        }
        // fully specified 
        /** Fully specified constructor that takes in a name and a drivers license number 
         *  @param n a String for the name of the Person you want to create 
         *  @param DL an integer for the drivers license number of the Person
        */
        public Person(String n, int DL){
            m_name = n;
            m_DL = DL;
        }
    
        // COPY constructor 
        /** copy constructor, copies a pre-existing person's member variables 
         *  @param personToCopy is a pre-existing Person object that you want to copy 
        */
        public Person(Person personToCopy){
            this.m_name = personToCopy.m_name; // "this" is optional here 
            m_DL = personToCopy.m_DL;
        }
    
        // an accessor 
        /** 
         * An accessor for the name attribute
         * @return String m_name The value of the Person's name attribute 
         */
        public String getName(){
            return m_name;
        }
         /** 
         * An accessor for the Drivers License attribute
         * @return int m_DL The value of the Person's Drivers License number 
         */
        public int getDL(){
            return m_DL;
        }
        // a mutator
        /** 
         * To change the Person's name 
         * @param newName a String for the Person's new name
         */
        public void setName(String newName){
            m_name = newName;
        }
    
    
        // equals method
        // we do this with strings: "Elia".equals("Elia");  // "equals" checks for equality
        // not: "Elia" == "Elia" // using == with objects just compares the memory locations
        
        // creating our own equals method to tell Java what it means for two "Person" objects to be "equal"
        /** 
         * To compare two Person objects for equality 
         * Two Person objects are said to be equal iff their Drivers License numbers are the same 
         * @param o Any Object you want to compare to a Person 
         * @return boolean, true if two Person objects are equal and have the same Drivers License numbers, false otherwise 
         */
        public boolean equals(Object o){
            // first check to be efficient, we automatically know they are equal
            // check memory locatoins 
            if (o == this){ return true;} // "this" is the object that called the method, to the left of . in dot notation
            
            // next, check if o is an instance of calss Person
            if (!(o instanceof Person)){ return false;} // return false if o is not a Person object
    
            // at this point we know o is a Person
            // type cast o back into a Person 
            Person p = (Person) o; 
    
            // now we are ready to check member variables 
            return ((this.m_DL == p.m_DL) );// && this.m_name.equals(p.m_name)
        }
    
        // a toString method 
        // override Java's default toString that just prints the object's memory location
        public String toString(){
            String s = "";
            s += "Name: " + m_name + "\n";
            s += "Driver's license number: "+ m_DL + "\n";
            return s;
        }
    
    }