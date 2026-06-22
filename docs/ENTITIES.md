# Матрица сущностей, методов и стандартных полей

Только **стандартные поля** Bitrix24. `UF_*` и бизнес-маппинги — в пресетах.

## company (Контрагенты)

- Методы: `crm.company.list/get/add/update/delete`, `crm.company.fields`.
- Поля: `ID, TITLE, COMPANY_TYPE, INDUSTRY, REVENUE, CURRENCY_ID, ADDRESS, ADDRESS_CITY,
  ADDRESS_POSTAL_CODE, ADDRESS_COUNTRY, PHONE, EMAIL, WEB, ASSIGNED_BY_ID, OPENED,
  COMMENTS, DATE_CREATE, DATE_MODIFY`.

## requisite (Реквизиты)

- Методы: `crm.requisite.list/get/add/update` (+ `crm.requisite.bankdetail.*`).
- Поля пресета реквизитов: `RQ_INN`, `RQ_KPP`, `RQ_OGRN`, `RQ_COMPANY_NAME`.
- `CompaniesDomain.get_inn_kpp(company_id)` — удобный доступ к ИНН/КПП для дедупа (`b24-sap`).

## product (Материалы)

- Методы: `catalog.product.list/get/add/update`, `catalog.product.fields`.
- Поля: `id, iblockId, name, code, active, measure, iblockSectionId, detailText, previewText`.
- Конфиг: `iblock_id`.

## price (Цены)

- Методы: `catalog.price.list/add/update`, типы цен `catalog.priceType.list`.
- Поля: `id, productId, catalogGroupId, price, currency`.
- Конфиг: `price_type_id`.

## store (Склады)

- Методы: `catalog.store.list/get`.
- Поля: `id, title, active, address`.

## store_product (Остатки)

- Методы: `catalog.storeproduct.list/get/add/update`.
- Поля: `id, storeId, productId, amount, quantityReserved`.

## deal (Сделки)

- Методы: `crm.deal.list/get/add/update/delete`, `crm.deal.fields`.
- Поля: `ID, TITLE, CATEGORY_ID, STAGE_ID, COMPANY_ID, CONTACT_ID, OPPORTUNITY, CURRENCY_ID,
  ASSIGNED_BY_ID, BEGINDATE, CLOSEDATE, CLOSED, OPENED, COMMENTS, DATE_CREATE, DATE_MODIFY`.

## deal_productrows (Товарные строки сделки)

- Методы: `crm.deal.productrows.get/set`.
- Поля: `PRODUCT_ID, PRODUCT_NAME, PRICE, QUANTITY, MEASURE_CODE`.

## События (subscribe)

| Событие коробки | Сущность | Действие |
|-----------------|----------|----------|
| `ONCRMCOMPANYADD/UPDATE/DELETE` | company | add/update/delete |
| `ONCRMDEALADD/UPDATE/DELETE` | deal | add/update/delete |
| `ONCRMCONTACTADD/UPDATE` | contact | add/update |

Каталог/остатки событий не имеют → **pull** по расписанию пресета.
