(ns sim)

(def stores
  {:building-supplies {:nails {:items {:metal 2}
                               :time 4}
                       :planks {:items {:wood 2}
                                :time 24}
                       :bricks {:items {:minerals 2}
                                :time 16}
                       :cement {:items {:minerals 2
                                        :chemicals 1}
                                :time 40}
                       :glue {:items {:plastic 1
                                      :chemicals 2}
                              :time 48}
                       :paint {:items {:metal 2
                                       :minerals 1
                                       :chemicals 2}
                               :time 48}}
   :hardware {:hammer {:items {:metal 1
                               :wood 1}
                       :time 11.2}
              :measuring-tape {:items {:metal 1
                                       :plastic 1}
                               :time 16}
              :shovel {:items {:metal 1
                               :wood 1
                               :plastic 1}
                       :time 24}
              :cooking-utensils {:items {:metal 2
                                         :wood 2
                                         :plastic 2}
                                 :time 36}
              :ladder {:items {:metal 2
                               :planks 2}
                       :time 48}
              :drill {:items {:metal 2
                              :plastic 2
                              :electrical-components 1}
                      :time 96}}
   :fashion {:cap {:items {:textiles 2
                           :measuring-tape 1}
                   :time 51}
             :shoes {:items {:textiles 2
                             :plastic 1
                             :glue 1}
                     :time 63}
             :watch {:items {:plastic 2
                             :glass 1
                             :chemicals 1}
                     :time 76}
             :business-suits {:items {:textiles 3
                                      :measuring-tape 1
                                      :glue 1}
                              :time 178}
             :backpack {:items {:textiles 2
                                :plastic 2
                                :measuring-tape 1}
                        :time 127}}
   :furniture {:chairs {:items {:wood 2
                                :nails 1
                                :hammer 1}
                        :time 16}
               :tables {:items {:planks 1
                                :nails 2
                                :hammer 1}
                        :time 24}
               :home-textiles {:items {:textiles 2
                                       :measuring-tape 1}
                               :time 60}
               :cupboard {:items {:planks 2
                                  :glass 2
                                  :paint 1}
                          :time 36}
               :couch {:items {:textiles 3
                               :drill 1
                               :glue 1}
                       :time 120}}
   :farmers-market {:beef {:items {:animal-feed 3}
                           :time 120}
                    :vegetables {:items {:seeds 2}
                                 :time 16}
                    :flour-bag {:items {:seeds 2
                                        :textiles 2}
                                :time 24}
                    :fruit-and-berries {:items {:seeds 2
                                                :tree-saplings 1}
                                        :time 72}
                    :cream {:items {:animal-feed 1}
                            :time 60}
                    :corn {:items {:minerals 1
                                   :seeds 4}
                           :time 48}
                    :cheese {:items {:animal-feed 2}
                             :time 84}}
   :gardening-supplies {:grass {:items {:seeds 1
                                        :shovel 1}
                                :time 24}
                        :tree-saplings {:items {:seeds 2
                                                :shovel 1}
                                        :time 72}
                        :garden-furniture {:items {:planks 2
                                                   :plastic 2
                                                   :textiles 2}
                                           :time 108}
                        :fire-pit {:items {:bricks 2
                                           :shovel 1
                                           :cement 2}
                                   :time 202}
                        :lawn-mower {:items {:metal 3
                                             :paint 1
                                             :electrical-components 1}
                                     :time 96}
                        :garden-gnomes {:items {:cement 2
                                                :glue 1}
                                        :time 72}}
   :donut-shop {:donuts {:items {:flour-bag 1
                                 :sugar-and-spices 1}
                         :time 38.25}
                :green-smoothie {:items {:vegetables 1
                                         :fruit-and-berries 1}
                                 :time 25.5}
                :bread-roll {:items {:flour-bag 2
                                     :cream 1}
                             :time 51}
                :cherry-cheesecake {:items {:flour-bag 1
                                            :fruit-and-berries 1
                                            :cheese 1}
                                    :time 76}
                :frozen-yogurt {:items {:fruit-and-berries 1
                                        :cream 1
                                        :sugar-and-spices 1}
                                :time 204}
                :coffee {:items {:cream 1
                                 :seeds 2
                                 :sugar-and-spices 1}
                         :time 51}}
   :fast-food {:ice-cream-sandwich {:items {:bread-roll 1
                                            :cream 1}
                                    :time 12.6}
               :pizza {:items {:flour-bag 1
                               :cheese 1
                               :beef 1}
                       :time 21.6}
               :burgers {:items {:beef 1
                                 :bread-roll 1
                                 :bbq-grill 1}
                         :time 31.5}
               :cheese-fries {:items {:vegetables 1
                                      :cheese 1}
                              :time 18}
               :lemonade-bottle {:items {:fruit-and-berries 1
                                         :glass 2
                                         :sugar-and-spices 2}
                                 :time 54}
               :popcorn {:items {:microwave-oven 1
                                 :corn 2}
                         :time 27}}
   :home-appliances {:bbq-grill {:items {:metal 3
                                         :cooking-utensils 1}
                                 :time 148}
                     :refrigerator {:items {:plastic 2
                                            :chemicals 2
                                            :electrical-components 2}
                                    :time 189}
                     :lighting-system {:items {:chemicals 1
                                               :electrical-components 1
                                               :glass 1}
                                       :time 94}
                     :tv {:items {:plastic 2
                                  :glass 2
                                  :electrical-components 2}
                          :time 135}
                     :microwave-oven {:items {:metal 4
                                              :glass 1
                                              :electrical-components 1}
                                      :time 108}}})

(defn item [k]
  (some #(get-in stores [% k])
        (keys stores)))

(def prod
  [:beef :couch :couch :coffee :coffee :coffee :hammer :hammer :hammer :business-suits :popcorn :popcorn :popcorn :microwave-oven :microwave-oven :paint :paint :paint :tree-saplings :tree-saplings :business-suits])

(defn items [l]
  (reduce into []
          (map
           #(:items (item %)) l)))

(defn n [item l]
  (reduce + (map last
                 (filter #(= item (first %))
                         (items l)))))

(def materials [:metal :wood :plastic :seeds :minerals :chemicals :textiles :sugar-and-spices :glass :animal-feed :electrical-components])

(for [m materials] 
  {m (n m prod)})

(n :metal prod)
