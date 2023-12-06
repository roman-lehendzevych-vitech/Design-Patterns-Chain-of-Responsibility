# Design Patterns: Chain of Responsibility

### 1. Quick idea about this pattern/Problem which this pattern solve?
Chain of Responsibility is a behavioral design pattern that lets you pass requests along a chain of handlers. Upon receiving a request, each handler decides either to process the request or to pass it to the next handler in the chain.

This pattern solve problem such as: When checks must be performed sequentially. Chain of Responsibility relies on transforming particular behaviors into stand-alone objects called handlers.
### 2. Where should we use this pattern (examples)?
When we have different ways of processing some data or need to execute several handlers in a particular order.
### 3. Pros and Cons
Pros:
- You can control the order of request handling.
- You can decouple classes that invoke operations from classes that perform operations.
- You can introduce new handlers into the app without breaking the existing client code.

Cons:
- Some requests may end up unhandled.
