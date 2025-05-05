# Copy and Move Semantics

```
class my_string {
  char* ptr;
  size_t capacity;
  size_t length;
}
```

The semantics of copy requires us to make a full copy of the string, involving the allocation
of another array in dynamic memory and copying of the ```*ptr's``` content there, which is expensive.

The semantics of move requires us only to transfer the value of ```*ptr ``` itself to new object
without duplicating the contents of the string. 

If the class doesn't use dynamic memory or system resources then there is no difference between
moving and copying in terms of performance.

Box::Box(const Box& other) 
{
  this->p = new HeavyResource(*(other.p)); // costly copying
}

Box::Box(Box && other)
{
  this->p = other.p // trivial stealing, part 1
  other.p = nullptr; // trivial stealing, part 2
}
