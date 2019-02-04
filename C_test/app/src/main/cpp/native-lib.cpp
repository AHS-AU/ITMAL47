#include <jni.h>
#include <string>

int i = 0;

extern "C" JNIEXPORT jstring JNICALL
Java_com_example_c_1test_MainActivity_stringFromJNI(
        JNIEnv *env,
        jobject /* this */) {
    i++;
    if( i % 2 == 0 )
    {
        std::string hello = "Hello from C++";
    } else {
        std::string hello = "get outta here!";
    }

    return env->NewStringUTF(hello.c_str());
}
