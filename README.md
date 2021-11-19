# Decrypt webdao v2ray

XOR

`key = yyyymmdd*4`

```
app-armeabi-v7a-release.apk

smali_classes2\xyz\webdao\v2ray\util\EncryptUtil.smali smali_classes2\xyz\webdao\v2ray\util\HttpUtil.smali
```

```java
byte[] decode = Base64.getDecoder().decode(node);
String node1 = new String(decode);
char[] charArray = key.toCharArray();
StringBuilder sb = new StringBuilder();
int length = node1.length();
for (int i = 0; i < length; i++) {
    sb.append((char) (node1.charAt(i) ^ charArray[i % charArray.length]));
}
```
