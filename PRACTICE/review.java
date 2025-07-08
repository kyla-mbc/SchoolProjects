public class review {
    // method:
    // public static dataTypeOfOutput methodName (dataType param1, dataType param2){}

    public static void multiplesOfFive (int[] array){
        // allocate multiples of 5 to each element in this array 
        for (int idx = 0; idx < array.length; ++idx){
            array[idx] = idx * 5;
        }
        // return array;
    }
    // overloaded methods: when we have multiple methods within the same class with the same name 
    // but different parameter lists 
    // either different types of parameters or a different amount of parameters 
    public static void multiplesOfFive (int[][] array){
        // allocate multiples of 5 to each element in this array 
        for (int r = 0; r < array.length; ++r){
            for (int c = 0; c < array[0].length; ++c){
                array[r][c] =  r * c * 5;
            }
        }
    }
    public static void printArray (int[] array){
        System.out.println("array inside method: ");
        System.out.println(array);
        for (int idx = 0; idx < array.length; ++idx){
            System.out.print(array[idx] + "  ");
        }
        System.out.println();
    }

    public static void printArray (int[][] array){
        for (int r = 0; r < array.length; ++r){
            for (int c = 0; c < array[0].length; ++c){
                System.out.print(array[r][c] + "  ");
            }
            System.out.println();
        }
    }

    public static void multiplesOfFive(int x){
        x = 5;
    }
    public static void main(String[] args) {
        // contiguous blocks of memory 
            // accessing elements at certain/ given indices is very fast 
        
        // syntax for a 1D array 
        // dataType[] identifier = new dataType[length]; // length = number of elements to be stored 
        int[] intArray = new int[15];
        System.out.println(intArray);
        printArray(intArray);
        multiplesOfFive(intArray); 
        printArray(intArray);

        int a = 9;
        multiplesOfFive(a);
        System.out.println(a);


    }
}
