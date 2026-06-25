ALTER TABLE product
ADD COLUMN IF NOT EXISTS discount_percent NUMERIC(5,2) NOT NULL DEFAULT 0;

ALTER TABLE product
ADD CONSTRAINT chk_discount_range
CHECK (discount_percent >= 0 AND discount_percent <= 100);

SELECT id, name, price, discount_percent FROM product;