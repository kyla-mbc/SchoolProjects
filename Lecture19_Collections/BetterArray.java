/**
 * a wrapper class for an array
 * giving an interface to an array to make arrays easier 
 */
public class BetterArray {
    // Member variables
    private int m_maxSize;
    private String[] m_arr;
    private int m_currentSize;

    // Default constructor
    public BetterArray() {
        m_maxSize = 100;
        m_arr = new String[m_maxSize];
        m_currentSize = 0;    }

    // Overloaded constructor
    public BetterArray(int maxSize) {
        m_maxSize = maxSize;
        m_arr = new String[m_maxSize];
        m_currentSize = 0;
    }

    // Getters 
    public int getMaxSize() {
        return m_maxSize;
    }

    public int getCurrentSize() {
        return m_currentSize;
    }

    // Add an element to the array
    public void add(String element) {
        if (m_currentSize == m_maxSize) {
            System.out.println("Re-size array!");
            String[] newArr = new String [2 * m_maxSize];
            for (int i = 0; i < m_maxSize; i++ ){
                newArr[i] = m_arr[i]; // copy everything from original, m_arr into new and bigger array.
            }
            m_arr = newArr; //shallow copy or change of reference. 
            m_maxSize = 2*m_maxSize; // set the max size to the new max size (double the original)
            /*
                your code here
                TO DO: 
                
                create a new array and set its maxSize to 2 * the current m_maxSize. 
                Do not change m_currentSize!

                e.g. if m_maxSize is = 100 currently, m_maxSize should be changed to 200 

                then, copy over all the elements of the old array into the new, bigger array
                
             */ 
        } 
        m_arr[m_currentSize] = element;
        ++m_currentSize;
    }

    // toString method to print the elements
    public String toString() {
        String s = "";
        for (int i = 0; i < m_currentSize; i++) {
            s += m_arr[i] + " ";
        }
        return s;
    }

    // equals method to check if two BetterArrays are equal
    public boolean equals(Object other) {
        // check if other is the same object (memory location) as this
        if (other == this) {
            return true;
        }
        // check if other is an instance of BetterArray
        if(!(other instanceof BetterArray)){
            return false;
        }
        // type cast other back into a BetterArray
        BetterArray bttr = (BetterArray) other; 
        // check if sizes are the same
        if (bttr.m_currentSize != m_currentSize) {
            return false;
        }
        // iterate through both BetterArrays' m_arr and check if all Strings are equal
        for (int i = 0; i < m_currentSize; i++) {
            // if a String at any point is not equal to a String in the same position of the 
            // other array, return false 
            if (!m_arr[i].equals(bttr.m_arr[i])) {
                return false;
            }
        }

        return true;
    }
}