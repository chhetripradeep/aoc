(defn read-input
  [filename]
  (->> filename
       slurp
       clojure.string/split-lines
       (map #(Integer/parseInt %))))

(defn get-triplets
  [numbers]
  (let [drop-1 (drop 1 numbers)
        drop-2 (drop 2 numbers)
        triplet(map vector numbers drop-1 drop-2)]
    triplet))

(defn calculate
  [numbers]
  (let [upper (drop 1 numbers)
        lower (drop-last 1 numbers)
        pairs (map vector lower upper)
        r (atom 0)]
    (for [p pairs]
      (if (< (first p) (last p))
        (swap! r inc)))))

(defn get-sum
  [v]
  (reduce + v))

(defn main
  []
  (let [numbers (read-input "input.txt")
        triplets (get-triplets numbers)
        sum-triplets (map get-sum triplets)
        result (calculate sum-triplets)]
    (last result)))

(print (main))
