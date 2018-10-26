


public class CircularArray implements Iterable<T> {

    private final List<T> list = new ArrayList<T>();
    private int length;
    private int baseIndex;

    public T getIndex(int index) {

    }

    public void setIndex(int index, T value) {

    }

    @Override
    public Iterator<T> iterator() {
        return new Iterator<T> () {
            private final Iterator<T> iter = list.iterator();

            @Override
            public boolean hasNext() {
                return iter.hasNext();
            }

            @Override
            public Book next() {
                return iter.next();
            }

            @Override
            public void remove() {
                throw new UnsupportedOperationException("no changes allowed");
            }
        };
    }

    public static void main(String[] args) {
        // Init array
        CircularArray<String> strings = new CircularArray<String>();
        strings.setIndex(0, "A");
        strings.setIndex(0, "B");
        strings.setIndex(0, "C");
        strings.setIndex(0, "D");
        // Print array
        for(String s : strings) {
            System.out.println(s);
        }
    }
}