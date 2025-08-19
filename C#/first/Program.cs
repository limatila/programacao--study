// See https://aka.ms/new-console-template for more information
Console.WriteLine("Hello, World!");

// namespace First.Animals
// {
//     public class Dog
//     {
//         public string Name { get; set; }
//         public int Id { get; set; }
//     }
// }

// Instantiating dog using its constructor
Dog dog = new Dog("Felermino", 2);
Dog dog2 = new Dog("Filipino", 7);

// barking
dog.Bark();
dog2.Bark();

public class Dog
{
    protected string Name { get; set; }
    protected int Age { get; set; }
    public Dog(string name, int age)
    {
        Name = name;
        Age = age;
    }

    // methods
    public void Bark()
    {
        if (Age < 5)
        {
            Console.WriteLine(Name + ": au");
        }
        else
        {
            Console.WriteLine(Name + ": AAAUUU");
        }
    }

}
