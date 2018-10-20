

public class Bar extends Thread {

    Foo myFoo;
    int id;

    public Bar(Foo myFoo, int id) {
        this.myFoo = myFoo;
        this.id = id;
    }

    @Override
    public void run() {
        switch(id) {
            case 0:
                myFoo.first();
                break;
            case 1:
                myFoo.second();
                break;
            case 2:
                myFoo.third();
                break;
            default:
                break;
        }
    }

    public static void main(String[] args) {
        
        Foo f = new Foo();
        
        Bar b1 = new Bar(f,0);
        Bar b2 = new Bar(f,1);
        Bar b3 = new Bar(f,2);

        b1.start();
        b2.start();
        b3.start();
    }
}