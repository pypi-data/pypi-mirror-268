# trubrics-sdk

> [!IMPORTANT]
> We are currently in beta.

To track events:

```python
trubrics = Trubrics(api_key="YOUR_TRUBRICS_API_KEY")

trubrics.track(
    event="User prompt",
    user_id="test_user_id",
    properties={"$text": "Hello, Trubrics! Tell me a joke?", "$thread_id": "your thread id"},
)
```
