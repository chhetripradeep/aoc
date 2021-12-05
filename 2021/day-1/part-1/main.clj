(defn read-input
  [filename]
  (->> filename
       slurp
       clojure.string/split-lines
       (map #(Integer/parseInt %))))

(defn calculate
  [numbers]
  (let [upper (drop 1 numbers)
        lower (drop-last 1 numbers)
        pairs (map vector lower upper)
        r (atom 0)]
    (for [p pairs]
      (if (< (first p) (last p))
        (swap! r inc)))))

(defn main
  []
  (let [numbers (read-input "input.txt")
        result (calculate numbers)]
    (last result)))

(print (main))
