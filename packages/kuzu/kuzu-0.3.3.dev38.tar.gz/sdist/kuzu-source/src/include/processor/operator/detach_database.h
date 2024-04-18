#pragma once

#include "processor/operator/database_operator.h"

namespace kuzu {
namespace processor {

class DetachDatabase final : public DatabaseOperator {
public:
    DetachDatabase(std::string dbName, uint32_t id, const std::string& paramsString)
        : DatabaseOperator{PhysicalOperatorType::DETACH_DATABASE, std::move(dbName), id,
              paramsString} {}

    bool getNextTuplesInternal(ExecutionContext* context) override;

    std::unique_ptr<PhysicalOperator> clone() override {
        return std::make_unique<DetachDatabase>(dbName, id, paramsString);
    }
};

} // namespace processor
} // namespace kuzu
