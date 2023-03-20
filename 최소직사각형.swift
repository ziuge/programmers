import Foundation

func solution(_ sizes:[[Int]]) -> Int {

    var w = 0
    var h = 0

    for i in sizes {
        var j = i.sorted()
        w = max(w, j[0])
        h = max(h, j[1])
    }

    return w * h
}
