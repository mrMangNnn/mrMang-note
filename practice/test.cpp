#include "iostream"

using namespace std;

class Shape
{
    public:
        Shape(int, int);
        virtual int area();
    protected:
        int width;
        int height;
};

Shape::Shape(int wid=0, int hig=0)
{
    width = wid;
    height = hig;
}

int Shape::area()
{
    cout << "Parent class area :"  << endl;
    return 0;
}

class Rectangle : public Shape
{
    public:
        Rectangle(int, int);
        int area()
        {
            cout << "Rectangle class area :";
            return (width * height);
        }
};

Rectangle::Rectangle(int wid=0, int hig=0):Shape(wid, hig){}

class Triangle : public Shape
{
    public:
        Triangle(int, int);
        int area()
        {
            cout << "Triangle class area :";
            return (width * height);
        }
};

Triangle::Triangle(int wid=0, int hig=0):Shape(wid, hig){}

int main()
{
    Shape *shape;
    Rectangle rec(10,7);
    Triangle tri(10,5);

    shape = &rec;
    cout << shape->area() << endl;

    shape = &tri;
    cout << shape->area() << endl;

    return 0;
}