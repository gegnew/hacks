class CreateForecasts < ActiveRecord::Migration[5.2]
  def change
    create_table :forecasts do |t|
      t.string :source
      t.string :forecast

      t.timestamps
    end
  end
end
