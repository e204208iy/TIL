## Option型
RustにはNullが存在しない代わりにOption型が存在する。
```rust
fn main() {
  let a: Option<i32> = Some(1);
  let b: Option<&str> = Some("str");
  let c: Option<i32> = None;

  let v:Vec<i32> = vec![1,2,3];
  let val: Option<&i32> = v.get(index:2);

  match val {
    Some(x: &i32) => println!("value exists: {}",x),
    None => println!("value is None"),
  }
}
```
