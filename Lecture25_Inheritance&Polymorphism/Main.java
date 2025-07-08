/**
INHERITANCE AND POLYMORPHISM

AGENDA:
We will build the following classes:
	- Instrument: which has a name, an origin, and price.
	- Guitar: which extends from Instrument and has a number of strings.
	- Drum: which extends from Instrument and has a number of pieces.

All classes have a default, overloaded, and copy constructor
as well as accessors, mutators, a toString() method,
and a play() method that prints an appropriate message
for the instrument to standard output.
*/

import java.util.LinkedList;

import javax.sound.midi.Instrument;
import javax.sound.sampled.Line;
public class Main {
    public static void main(String[] args) {
        Guitar g1 = new Guitar(5, "Spanish", "Spain", 800);
        System.out.println(g1);
        Guitar g2 = new Guitar();
        Guitar g1Copy = new Guitar(g1);
        System.out.println(g1.equals(g2));
        System.out.println(g1.equals(g1Copy));


        Drum d1 = new Drum(9, "Cool", "China", 978);
        System.out.println(d1);
        Drum d2 = new Drum();
        Drum d1Copy = new Drum(d1);
        System.out.println(d1.equals(d2));
        System.out.println(d1.equals(d1Copy));


        LinkedList<Instrument1> myInstruments = new LinkedList<>();
        myInstruments.add(g1);
        myInstruments.add(d1);
        myInstruments.add(g1Copy);
        myInstruments.add(d1Copy);
        myInstruments.add(g2);
        myInstruments.add(d2);

        // myInstruments.get(2).play(); // this calls the play method from 

        // for (Instrument1 i: myInstruments){
        //     i.play(); // late binding - will call the specific object;s play method, not Instrument1's play method
        // }

        /*
         * POLYMORPHISM = "multiple forms"
         * Every object can take on many forms 
         * 
         * LATE BINDING -> at runtime, Java will look for and 
         *  run the most specific version of a method for a given object 
         * 
         */

        /**
         * ABSTRACT CLASSES
         * are classes that exist for the purpose of inheritance
         * and cannot be instantiated
         * they are just a concept/group of other more concrete objects
         */
        Instrument1 i = new Guitar();
        System.out.println(i);

        i = new Drum();

        Percussion x = new Drum();



    }
}
