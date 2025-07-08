public class MirrorFlipImage{

    private static void displayImage(char[][] image) {
        for (int r = 0; r < image.length; r++){
            for (int c = 0; c < image[0].length; c++){
                System.out.print(image[r][c] + " ");
            }
            System.out.println();
        }

    }
    private static char[][] horizontalMirror(char[][] image){
        char[][] hArray = new char [image.length][image[0].length];
        for (int r = 0; r < image.length; r++){
            for (int c = 0; c < image[0].length; c++){
                hArray[r][c] = image[image.length - 1 - r][c];
            }
        }
        return hArray;
    }
    private static char[][] verticalMirror(char[][] image){
        char[][] vArray = new char[image.length][image[0].length];
        for (int r = 0; r < image.length; r++){
            for (int c = 0; c< image[0].length; c++){
                vArray[r][c] = image[r][image[0].length - 1 - c];
            }
        }
        return vArray;
    }

    public static void main(String[] args) {
        char[][] image = {
            {'#', 'M', '#', '#', '#'},
            {'#', ' ', ' ', ' ', '#'},
            {'#', ' ', 'K', ' ', '#'},
            {'*', ' ', ' ', ' ', 'B'},
            {'#', ' ', ' ', ' ', '#'},
            {'#', ' ', ' ', ' ', '#'},
            {'#', '#', '#', 'C', '#'},
        }; 

        System.out.println("Original Image:");
        displayImage(image);

        System.out.println("Horizontally flipped image:");
        displayImage(horizontalMirror(image));

        System.out.println("Vertically flipped image:");
        displayImage(verticalMirror(image));

        System.out.println("Horizontally and then Vertically flipped image:");
        displayImage(horizontalMirror(verticalMirror(image)));

    }
}