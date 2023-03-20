func solution(_ n:Int) -> Int {

    return fibo(n) % 1234567
}

func fibo(_ a: Int) -> Int {
    if a < 2 {
        return a
    }

    var cache = [Int](repeating: 0, count: a+1)
    cache[1] = 1

    for i in (2...a) {
        cache[i] = (cache[i - 1] % 1234567) + (cache[i - 2] % 1234567)
    }

    return cache[a]
}
