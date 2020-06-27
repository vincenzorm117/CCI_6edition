

public class Foo {
    public Foo() {}

    private int order = 0;

    private void check(int id) {
        while(order != id ) ;
    }
    private void increment() {
        this.order = (this.order + 1) % 3;
    }

    public void first() {
        check(0);
        System.out.println("Running first");
        increment();
    }
    public void second() {
        check(1);
        System.out.println("Running second");
        increment();
    }
    public void third() {
        check(2);
        System.out.println("Running third");
        increment();
    }

}