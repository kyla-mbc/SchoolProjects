/*
Abstract class called Pokemon that also implements the Comparable interface
*/
public abstract class Pokemon implements Comparable<Pokemon> {

    /*
    Protected Member Variables that represent the name, type, level, health, attack, and defense of the Pokemon (Use of protected key word so that the child classes can access these variables)
    */
    protected String m_name;
    protected String m_type;
    protected int m_level;
    protected int m_health;
    protected int m_attack;
    protected int m_defense;

    /*
    Default Constructor that initializes the name, type, level, health, attack, and defense of the Pokemon
    */
    public Pokemon() {
        m_name = null;
        m_type = null;
        m_level = 1;
        m_health = 10;
        m_attack = 5;
        m_defense = 10;
    }

    /*
    Fully Specified Constructor that initializes the name, type, level, health, attack, and defense using the parameters
    @param n - name of the Pokemon
    @param t - type of the Pokemon
    @param l - level of the Pokemon
    @param h - health of the Pokemon
    @param a - attack of the Pokemon
    @param d - defense of the Pokemon
    */
    public Pokemon(String n, String t, int l, int h, int a, int d) {
        m_name = n;
        m_type = t;
        m_level = l;
        m_health = h;
        m_attack = a;
        m_defense = d;
    }

    /*
    The 6 methods below are getter methods that return the name, type, level, health, attack, and defense of the Pokemon
    @return m_name - the name of the Pokemon
    @return m_type - the type of the Pokemon
    @return m_level - the level of the Pokemon
    @return m_halth - the health of the Pokemon
    @return m_attack - the attack of the Pokemon
    @return m_defense - the defense of the Pokemon
    */
    public String getName() {
        return m_name;
    }

    public String getType() {
        return m_type;
    }

    public int getLevel() {
        return m_level;
    }

    public int getHealth() {
        return m_health;
    }

    public int getAttack() {
        return m_attack;
    }

    public int getDefense() {
        return m_defense;
    }

    /*
    The 6 methods below are setter methods that set the new name, type, level, health, attack, and defense of the Pokemon
    @param n - the new name of the Pokemon
    @param t - the new type of the Pokemon
    @param l - the new level of the Pokemon
    @param h - the new health of the Pokemon
    @param a - the new attack of the Pokemon
    @param d - the new defense of the Pokemon
    */
    public void setName(String n) {
        m_name = n;
    }

    public void setType(String t) {
        m_type = t;
    }

    public void setLevel(int l) {
        m_level = l;
    }

    public void setHealth(int h) {
        m_health = h;
    }

    public void setAttack(int a) {
        m_attack = a;
    }

    public void setDefense(int d) {
        m_defense = d;
    }

    /*
    Method to create a nicely printed statement, that prints all of the Pokemon's information
    Overridden in the child classes
    @return s - a string containing the Pokemon's name, type, level, health, attack, and defense
    */
    @Override
    public String toString() {
        String s = "";
        s += "Name: " + m_name + "\n";
        s += "Type: " + m_type + "\n";
        s += "Level: " + m_level + "\n";
        s += "Health: " + m_health + "\n";
        s += "Attack: " + m_attack + "\n";
        s += "Defense: " + m_defense + "\n";
        return s;
    }

    /*
    Method that checks if two Pokemon are equal
    @param o - the object to be compared to the current object
    @return t - true if the objects are equal, false if they are not
    @return m_name.equals(p.m_name) &&
                m_type.equals(p.m_type) &&
                m_level == p.m_level &&
                m_health == p.m_health &&
                m_attack == p.m_attack &&
                m_defense == p.m_defense - checks if all of the member variables are equal
    */
    public boolean equals(Object o) {
        if (this == o) {
            return true;
        }
        if (!(o instanceof Pokemon)) {
            return false;
        }
        Pokemon p = (Pokemon) o;
        return m_name.equals(p.m_name) &&
                m_type.equals(p.m_type) &&
                m_level == p.m_level &&
                m_health == p.m_health &&
                m_attack == p.m_attack &&
                m_defense == p.m_defense;
    }

    /*
    Method that gets the total stats of a pokemon
    @return m_attack + m_defense + m_health - total stats of the Pokemon
    */
    public int getTotalStats() {
        return m_attack + m_defense + m_health;
    }

    /*
    Abstract method that would be defined in the child classes, simulating how the Pokemon would sound
    */
    public abstract void doCry();

    /*
    Method that compares two Pokemon based on their level
    @param p - the Pokemon to be compared to the current object
    @return -1 if the current object is less than the parameter, 0 if they are equal, and 1 if the current object is greater than
    */
    public int compareTo(Pokemon p) {
        if (m_level < p.m_level) {
            return -1;
        } else if (m_level > p.m_level) {
            return 1;
        } else {
            return 0;
        }
    }
}